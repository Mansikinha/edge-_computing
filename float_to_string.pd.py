import pandas as pd

# initialize list of lists
data = [['Harsh', 10, 45.25], ['Gerry', 15, 54.85],
        ['Juli', 14, 87.21], ['Ricky', 20, 45.23],
        ['Siya', 21, 77.25], ['Jessie', 16, 95.21]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age', 'Marks'],
                  index=['1', '2', '3', '4', '5', '6'])


print(df.dtypes)

# Now we will convert it from
# 'float' to 'String' type.
df['Marks'] = df['Marks'].astype(str)

print()

print(df.dtypes)


print(df)
