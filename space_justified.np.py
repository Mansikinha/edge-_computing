import numpy as np

x = np.array(['python ', 'PHP', 'java', 'C++'], dtype=str)  
print("Original Array:")
print(x)

centered = np.char.center(x, 15, fillchar='_')
left = np.char.ljust(x, 15, fillchar='_')
right = np.char.rjust(x, 15, fillchar='_')

print("\nCentered =", centered)
print("Left =", left)
print("Right =", right)
