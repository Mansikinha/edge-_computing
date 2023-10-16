import numpy as np

# Matrix multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
result_matrix_mul = np.matmul(matrix_a, matrix_b)

#element wise square root
result_sqrt = np.sqrt(matrix_a)

print("Matrix Multiplication:")
print(result_matrix_mul)
print("\nElement wise Square Root:")
print(result_sqrt)
