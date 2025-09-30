from transformers import pipeline
import os

# Caminho do modelo treinado
MODEL_PATH = "app/ai/EmailClassifier"

# Inicializa pipeline de classificação
classifier = pipeline(
    "text-classification",
    model=MODEL_PATH,
    tokenizer=MODEL_PATH
)

def predict_importance(subject: str, body: str) -> str:
    """
    Retorna a categoria do email: 'Produtivo' ou 'Improdutivo'
    """
    text = subject + " " + body
    result = classifier(text)[0]
    label = result["label"]

    # Ajuste conforme labels do seu dataset
    if label == "LABEL_1":
        return "Produtivo"
    return "Improdutivo"
