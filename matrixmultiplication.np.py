import numpy as np

# Create two matrices of complex numbers
matrix1 = np.array([1+2j, 3+4j])
matrix2 = np.array([5+6j, 7+8j])

result_matrix = np.sum( np.conjugate(matrix1* matrix2))

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nResult Matrix:")
print(result_matrix)
