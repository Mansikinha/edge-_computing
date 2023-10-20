import numpy as np

# Computing sine and cosine values
angles = np.array([0, np.pi/2, np.pi])
sin_values = np.sin(angles)
cos_values = np.cos(angles)

# Exponential and logarithmic functions
exp_values = np.exp(np.array([1, 2, 3]))
log_values = np.log(np.array([1, 2, 4]))

print("Sine Values:", sin_values)
print("Cosine Values:", cos_values)
print("Exponential Values:", exp_values)
print("Logarithmic Values:", log_values)
