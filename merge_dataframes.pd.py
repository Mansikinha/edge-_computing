import pandas as pd

# Sample DataFrames
data1 = {'common_column': [1, 2, 3, 4],
         'data1_col': ['A', 'B', 'C', 'D']}
data2 = {'common_column': [3, 4, 5, 6],
         'data2_col': [10, 20, 30, 40]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge the DataFrames on the common column
merged_df = pd.merge(df1, df2, on='common_column')

print(merged_df)
