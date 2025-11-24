import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Fixed version – generates correct shapes
np.random.seed(42)
common_weak = ["123456", "password", "123456789", "12345", "qwerty", "abc123", "password123", "admin"]
strong_patterns = ["Tr0ub4dor&3", "P@ssw0rd2025!", "K9.m0v1e#star2025", "Guitar!99Hero"]

def generate_passwords(n_weak=90000, n_strong=10000):
    weak = []
    for _ in range(n_weak):
        base = np.random.choice(common_weak)
        suffix = np.random.choice(["", "1", "123", "!", "@", "2024", "2025"])
        prefix = np.random.choice(["", "a", "A", "my", "letmein"])
        weak.append(prefix + base + suffix)
    
    strong = []
    for _ in range(n_strong):
        length = np.random.randint(12, 25)
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        strong.append(''.join(np.random.choice(list(chars), length)))
    
    passwords = weak + strong
    labels = [0] * len(weak) + [1] * len(strong)
    return passwords, labels

print("Generating training data...")
X, y = generate_passwords()
df = pd.DataFrame({"password": X, "strength": y})

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(analyzer='char', ngram_range=(2,5))),
    ('clf', LogisticRegression(max_iter=1000))
])

print("Training model...")
pipeline.fit(df['password'], df['strength'])
joblib.dump(pipeline, 'password_model.pkl')
print("Model saved – ready to go!")