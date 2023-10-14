import numpy as np

# Create a random matrix
matrix = np.random.rand(3, 3)

# Perform SVD
U, S, V = np.linalg.svd(matrix)

print("Original Matrix:")
print(matrix)

print("\nU:")
print(U)

print("\nS:")
print(S)

print("\nV:")
print(V)
