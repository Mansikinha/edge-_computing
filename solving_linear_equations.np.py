import numpy as np

# Coefficient matrix
A = np.array([[2, 1], [1, -3]])

#righ hamd side vector
B = np.array([8, 1])

# Solve linear equations Ax = B
x = np.linalg.solve(A, B)

# Print the solution
print("Solution to Linear Equations:")
print(f"x = {x[0]}, y = {x[1]}")
