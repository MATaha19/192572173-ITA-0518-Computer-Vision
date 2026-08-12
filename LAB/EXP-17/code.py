import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\Mohammed Taha\OneDrive\Pictures\Chartwork\unnamed.webp", 0)

# Sobel X Edge Detection
sobel_x = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)

# Display original image
cv2.imshow("Original Image", img)

# Display Sobel X output
cv2.imshow("Sobel X Edge Detection", sobel_x)

# Save the output
cv2.imwrite("sobel_x.jpg", sobel_x)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
