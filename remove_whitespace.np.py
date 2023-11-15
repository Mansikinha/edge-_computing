import numpy as np

# Sample array with elements containing leading whitespaces
original_array = np.array(['  apple' , '        banana', 'cherry  ', ])

# Remove leading whitespaces
stripped_array = np.char.lstrip(original_array)

# Display the original and stripped arrays
print("Original Array:")
print(original_array)

print("\nRemove the Leading Whitespaces :")
print(stripped_array)
