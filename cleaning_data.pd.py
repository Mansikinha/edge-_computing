import pandas as pd

data = {
    'Name': ['Shyam', 'Boby', 'bruno', 'shyam', 'Ram'],
    'Age': [25, 30, None, 25, 35],
    'City': ['New York', 'Dubai', 'Las vegas', 'New York', 'mumbai'],
    'Salary': [50000, 60000, 70000, None, 80000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)
print("\n")

numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

#removing duplicates
df.drop_duplicates(inplace=True)

# Displaying the cleaned data
print("Cleaned Data:")
print(df)
