import pandas as pd

#creating data
data = {'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']}
df = pd.DataFrame(data)

#printing data frame
print("DataFrame:")
print(df)

#saving data frame to csv
df.to_csv('output.csv', index=False)

print("CSV file 'output.csv' has been created.")

