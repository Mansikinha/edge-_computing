
import numpy as np

# Create a sample 2D array
arr = np.array([[1, 5, 3],
                [8, 2, 4],
                [7, 6, 9]])

# Calculate the difference between the maximum and minimum values along the second axis (axis=1)
result = np.ptp(arr, axis=1)

# Print the result
print("Array:")
print(arr)
print("Difference between max and min along the second axis:")
print(result)


