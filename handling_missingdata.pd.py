import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eve', 'Frank'],
    'City': ['New York', 'Los Angeles', np.nan, 'Chicago', 'Houston', 'Miami'],
    'Age': [25, 30, 22, np.nan, 28, 32]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Replace missing string values with a default value, and drop rows with missing 'Age'
df.fillna({'Name': 'Unknown', 'City': 'Unknown'}, inplace=True)
df.dropna(subset=['Age'], inplace=True)

print("\nDataFrame after handling missing data:")
print(df)
