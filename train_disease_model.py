# train_disease_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os
from utils.disease_symptoms import SYMPTOM_COLS
# Load and clean CSV
csv_path = "my data/poultry_disease_data_cleaned.csv"
df = pd.read_csv(csv_path)
# Clean column names (remove spaces and lowercase)
df.columns = df.columns.str.strip().str.lower()
# Filter relevant columns
required_columns = SYMPTOM_COLS + ["diagnosis", "treatment"]
df = df[required_columns]
# Ensure features are numeric
X = df[SYMPTOM_COLS]
y = df["diagnosis"]
assert X.select_dtypes(include=["object"]).empty, "X contains non-numeric values!"
# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
# Evaluate
print("\n✅ Model Evaluation:\n")
print(classification_report(y_test, clf.predict(X_test)))
# Save model
os.makedirs("ml_models", exist_ok=True)
joblib.dump(clf, "ml_models/disease_model.pkl")
print("\n✅ Model saved to ml_models/disease_model.pkl")