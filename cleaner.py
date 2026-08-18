import pandas as pd

# 1. Raw Data ማንበብ
df = pd.read_csv('raw_data.csv')

# 2. Duplicate Data ማስወገድ
df = df.drop_duplicates()

# 3. ባዶ (Missing) ቦታዎችን መሙላት ወይም ማስወገድ
df = df.dropna()

# 4. የጸዳውን መረጃ በአዲስ CSV ፋይል ማስቀመጥ
df.to_csv('cleaned_data.csv', index=False)

print("Data cleaning successfully completed!")
