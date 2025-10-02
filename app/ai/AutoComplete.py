# app/ai/AutoComplete.py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("data/emails.csv")
texts = (df['subject'].fillna('') + ' ' + df['body'].fillna('')).str.lower().tolist()

# n-grams 1 a 3 palavras
vectorizer = CountVectorizer(ngram_range=(1,3))
X = vectorizer.fit_transform(texts)
X_sum = X.sum(axis=0).A1
ngram_freq = dict(zip(vectorizer.get_feature_names_out(), X_sum))

def autocomplete(text, n=5):
    text = text.lower()
    suggestions = [ng for ng in ngram_freq if ng.startswith(text)]
    suggestions.sort(key=lambda x: -ngram_freq[x])
    return suggestions[:n]
