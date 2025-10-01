import joblib
import os

# Carrega modelo treinado
MODEL_PATH = "app/ai/EmailClassifier/email_classifier.pkl"
classifier = joblib.load(MODEL_PATH)

PROMO_KEYWORDS = [
    "oferta", "imperdível", "desconto", "promoção", "frete grátis",
    "compre já", "liquidação", "ganhe", "promo"
]

def predict_importance(subject: str, body: str) -> str:
    text = f"{subject} {body}".lower()

    # Se tiver palavras-chave de promoção, considera improdutivo
    if any(kw in text for kw in PROMO_KEYWORDS):
        return "Improdutivo"

    pred = classifier.predict([text])[0]
    return "Produtivo" if pred == 1 else "Improdutivo"
