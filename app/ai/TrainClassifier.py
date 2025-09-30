import os
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

# ===== Configurações =====
DATA_PATH = "data/emails.csv"             # CSV de treino
MODEL_NAME = "distilbert-base-uncased"    # Modelo pré-treinado
OUTPUT_DIR = "app/ai/EmailClassifier"     # Onde salvar modelo

# Cria pasta se não existir
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Carrega dataset CSV
dataset = load_dataset("csv", data_files={"train": DATA_PATH}, delimiter=",")

# Tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Função para tokenizar
def tokenize(batch):
    return tokenizer(batch["subject"] + " " + batch["body"], padding=True, truncation=True)

dataset = dataset.map(tokenize, batched=True)
dataset.set_format("torch", columns=["input_ids", "attention_mask", "label"])

# Modelo
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)

# Argumentos de treinamento
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=3,
    per_device_train_batch_size=16,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_dir=os.path.join(OUTPUT_DIR, "logs"),
    logging_steps=10
)

# Treinador
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"]
)

# Treina
trainer.train()

# Salva modelo e tokenizer
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print(f"Modelo treinado e salvo em: {OUTPUT_DIR}")
