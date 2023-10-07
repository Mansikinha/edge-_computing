import pandas as pd

data = {'column1': [1, 2, 3, 4],
        'column2': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Create a new column based on existing columns
df['new_column'] = df['column1'] + df['column2']

print(df)
