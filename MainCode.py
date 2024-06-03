import cv2
import numpy as np

# Load the 3D image
image_path = 'your_image_here.png'  # Replace with your image path
image = cv2.imread(image_path)

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Edge detection using Canny
edges = cv2.Canny(blurred_image, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
floor_plan = np.zeros_like(image)
cv2.drawContours(floor_plan, contours, -1, (0, 255, 0), 1)

# Display the images
cv2.imshow('Original Image', image)
cv2.imshow('Floor Plan', floor_plan)
cv2.waitKey(0)
cv2.destroyAllWindows()
