import pandas as pd

#Create a DataFrame:
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 15, 25, 12, 18],
    'Quantity': [5, 10, 8, 12, 6, 9]
}

df = pd.DataFrame(data)

#Display the Original DataFrame:
print("Original DataFrame:")
print(df)
print("\n")


#Grouping and Calculating Mean:
grouped_df = df.groupby('Category').mean()


#Display the Grouped DataFrame with Mean Values:
print("Grouped DataFrame with Mean:")
print(grouped_df)
print("\n")

#Grouping and Aggregating with Custom Functions:
agg_df = df.groupby('Category').agg({
    'Value': 'sum',
    'Quantity': 'mean'
})


#Display the Aggregated DataFrame:
print("Aggregated DataFrame:")
print(agg_df)

print(df)


