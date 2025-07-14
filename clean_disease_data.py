import pandas as pd
# Load file
df = pd.read_csv("my data/poultry_disease_data.csv")
# Drop any rows with completely empty values
df.dropna(how='all', inplace=True)
# Strip spaces in column names
df.columns = [col.strip() for col in df.columns]
# Convert all symptom columns to integers
# We'll assume all columns except the last 2 are symptoms
symptom_columns = df.columns[:-2]
# Convert to 0/1 and ensure they're integers
for col in symptom_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
# Drop rows where any symptom is still NaN (invalid)
df.dropna(subset=symptom_columns, inplace=True)
# Convert symptom columns to int
df[symptom_columns] = df[symptom_columns].astype(int)
# Save cleaned version
df.to_csv("my data/poultry_disease_data_cleaned.csv", index=False)
print("✅ Cleaned CSV saved as 'my data/poultry_disease_data_cleaned.csv'")
print(f"\n✅ Cleaned rows: {len(df)}")
print("🔍 Sample cleaned data:")
print(df.head())
