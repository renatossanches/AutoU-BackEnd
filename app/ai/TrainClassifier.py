import os
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

PORTUGUESE_STOPWORDS = stopwords.words('portuguese')

# Configurações
DATA_PATH = "data/emails.csv"
OUTPUT_DIR = "app/ai/EmailClassifier"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Carrega dados
df = pd.read_csv(DATA_PATH)
df["text"] = (df["subject"].fillna("") + " " + df["body"].fillna("")).str.lower()

X = df["text"]
y = df["label"]

# Divide dados
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        max_features=10000,
        ngram_range=(1, 2),
        stop_words=PORTUGUESE_STOPWORDS
    )),
    ("clf", LogisticRegression(
        max_iter=500,
        solver="liblinear",
        class_weight="balanced"
    ))
])

# Treina
model.fit(X_train, y_train)

# Avaliação
y_pred = model.predict(X_test)
print("\n=== Relatório de Classificação ===")
print(classification_report(y_test, y_pred, target_names=["Improdutivo", "Produtivo"]))

# Validação cruzada
scores = cross_val_score(model, X, y, cv=5)
print(f"\nValidação cruzada média (5-fold): {scores.mean():.4f}")

# Salva modelo
joblib.dump(model, os.path.join(OUTPUT_DIR, "email_classifier.pkl"))
print(f"\nModelo salvo em: {OUTPUT_DIR}/email_classifier.pkl")
