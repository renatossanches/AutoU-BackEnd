import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Carrega emails
df = pd.read_csv("data/emails.csv")
texts = (df['subject'].fillna('') + ' ' + df['body'].fillna('')).str.lower().tolist()

# Cria n-grams (bi-gramas e tri-gramas)
vectorizer = CountVectorizer(ngram_range=(2, 3))
X = vectorizer.fit_transform(texts)

# Frequência de cada n-gram
ngram_freq = dict(zip(vectorizer.get_feature_names_out(), X.toarray().sum(axis=0)))

# Função de autocomplete
def autocomplete(text, n=5):
    text = text.lower()
    suggestions = [ng for ng in ngram_freq if ng.startswith(text)]
    suggestions.sort(key=lambda x: -ngram_freq[x])
    return suggestions[:n]
