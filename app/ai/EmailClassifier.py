import joblib
import os

# Carrega modelo treinado
MODEL_PATH = "app/ai/EmailClassifier/email_classifier.pkl"
classifier = joblib.load(MODEL_PATH)

def predict_importance(subject: str, body: str) -> str:
    text = f"{subject} {body}".lower()
    pred = classifier.predict([text])[0]
    return "Produtivo" if pred == 1 else "Improdutivo"
