import pandas as pd


data = {'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']}
df = pd.DataFrame(data)

print("DataFrame:")
print(df)

df.to_csv('output.csv', index=False)

print("CSV file 'output.csv' has been created.")
