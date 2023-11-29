import pandas as pd

s = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'])
print("String Date:")
print(s)

r = pd.to_datetime(s)  

df = pd.DataFrame({'Date': r})  

print("Original DataFrame (string to datetime):")
print(df)
