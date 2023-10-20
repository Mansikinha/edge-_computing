import numpy as np

# Simulate image data
image_data = np.random.randint(0, 255, size=(3, 3), dtype=np.uint8)

# Set a threshold for pixel values
threshold = 128

# Apply thresholding
binary_image = np.where(image_data > threshold, 255, 0).astype(np.uint8)

print("Image Data:")
print(image_data)
print("\nBinary Image (Thresholded):")
print(binary_image)
