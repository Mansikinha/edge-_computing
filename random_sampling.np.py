import numpy as np

# Set the stage for consistent randomness
np.random.seed(42)

# Generate 500 random numbers that could be anything
random_numbers = np.random.normal(loc=0, scale=1, size=500)

mean_value = np.mean(random_numbers)  
median_value = np.median(random_numbers)  
std_deviation = np.std(random_numbers)  # How spread out the numbers are
variance = np.var(random_numbers)  # Measure of how much the numbers deviate from the mean


print("First 60 Random Numbers:")
print(random_numbers[:25])  # Display the first 25 random numbers
print("\nWhat We Learned:")
print(f"Average (Mean): {mean_value}")
print(f"Middle Value (Median): {median_value}")
print(f"Spread (Standard Deviation): {std_deviation}")
print(f"Variety (Variance): {variance}")
