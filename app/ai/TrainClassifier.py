import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# ===== Configurações =====
DATA_PATH = "data/emails.csv"
OUTPUT_DIR = "app/ai/EmailClassifier"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===== Carrega dados =====
df = pd.read_csv(DATA_PATH)
df['text'] = df['subject'] + " " + df['body']

X = df['text']
y = df['label']  # 0 = Improdutivo, 1 = Produtivo

# ===== Divide dados =====
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ===== Pipeline TF-IDF + Naive Bayes =====
model = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000)),
    ('clf', MultinomialNB())
])

# Treina
model.fit(X_train, y_train)

# Avalia
accuracy = model.score(X_test, y_test)
print(f"Acurácia: {accuracy:.4f}")

# Salva modelo
joblib.dump(model, os.path.join(OUTPUT_DIR, "email_classifier.pkl"))
print(f"Modelo treinado salvo em: {OUTPUT_DIR}/email_classifier.pkl")
