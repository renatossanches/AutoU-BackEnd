import os
import joblib

# Caminho do modelo treinado
MODEL_PATH = "app/ai/EmailClassifier/email_classifier.pkl"

# Carrega modelo
classifier = joblib.load(MODEL_PATH)

def predict_importance(subject: str, body: str) -> str:
    """
    Retorna a categoria do email: 'Produtivo' ou 'Improdutivo'
    """
    text = subject + " " + body
    pred = classifier.predict([text])[0]
    return "Produtivo" if pred == 1 else "Improdutivo"