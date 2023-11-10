# importing required modules
import pandas as pd

dataframe = pd.DataFrame([[1, 'A', "Student"],
                          [2, 'B', "Tutor"],
                          [3, 'C', "Instructor"]])

print("Original DataFrame")
print(dataframe)

# reversing the dataframe
print("\nReversed DataFrame")
print(dataframe.iloc[:, ::-1])
