import numpy as np

# Define two polynomials
poly1 = np.poly1d([1, 2, 3])  # Represents x^2 + 2x + 3
poly2 = np.poly1d([4, 5, 6])  # Represents 4x^2 + 5x + 6

# Add and multiply polynomials
sum_poly = np.polyadd(poly1, poly2)
product_poly = np.polymul(poly1, poly2)

print("Sum of Polynomials:", sum_poly)
print("Product of Polynomials:", product_poly)
