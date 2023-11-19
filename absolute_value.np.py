import numpy as np

# create a Numpy array
arr = np.array([-10.2, -22.2, 16 ,  -35 ])

# calculate the absolute value element -wise 
abs_arr = np.abs(arr)

print("Original array:")
print(arr)
print("Element-wise absolute value:") 


print(np.absolute(arr))
