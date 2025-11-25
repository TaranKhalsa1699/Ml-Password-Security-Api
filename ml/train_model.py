import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
from ml.feature_engineering import create_features
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "passwords.csv")

df = pd.read_csv(DATA_PATH)


# Create features
df = create_features(df)

X = df[["length", "entropy", "rule_score"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Model trained!")

# Save model
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
pickle.dump(model, open(MODEL_PATH, "wb"))
print("model.pkl saved inside ml/ folder")
