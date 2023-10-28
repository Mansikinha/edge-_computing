

import pandas as pd

# Create or load your DataFrame
data = pd.DataFrame({'column_name': [1, 5, 15, 20],
                     'column1': [2, 6, 12, 18],
                     'column2': [3, 7, 13, 21]})

# Select a single column
column_data = data['column_name']

# Select multiple columns
subset = data[['column1', 'column2']]

# Select rows based on a condition
filtered_data = data[data['column_name'] >15]

# Show the output
print("Original DataFrame:")
print(data)
print("\nSelected single column 'column_name':")
print(column_data)
print("\nSelected subset of columns 'column1' and 'column2':")
print(subset)
print("\nSelected rows where 'column_name' is greater than 15:")
print(filtered_data)

