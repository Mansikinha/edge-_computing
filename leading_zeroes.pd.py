import pandas as pd

nums = {'amount': ['10', '250', '3000', '40000', '500000']}
df = pd.DataFrame(nums)

print("Original dataframe:")
print(df)

print("\nAdd leading zeros:")
df['amount'] = df['amount'].str.zfill(10)
print(df)
