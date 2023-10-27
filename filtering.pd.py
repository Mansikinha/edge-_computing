import pandas as pd

data = {'Name': ['Ammy', 'Ram', 'Shyam', 'Devi', 'Era'],
        'Age': [25, 30, 22, 35, 28],
        'Gender': ['M', 'M', 'M', 'F', 'F']}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Filter data in a shorter way
filtered_df_1 = df[df['Age'] > 25]
filtered_df_2 = df[(df['Age'] > 25) & (df['Gender'] == 'M')]

print("\nFiltered DataFrame (Age > 25):")
print(filtered_df_1)

print("\nFiltered DataFrame (Age > 25 and Gender is 'M'):")
print(filtered_df_2)
