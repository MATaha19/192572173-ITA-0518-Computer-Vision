import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\Mohammed Taha\OneDrive\Pictures\Chartwork\images (1).jpg", 0)

# Sobel Y edge detection
sobel_y = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=5)

# Save output
cv2.imwrite("sobel_y.jpg", sobel_y)

# Display original image
cv2.imshow("Original Image", img)

# Display Sobel Y output
cv2.imshow("Sobel Y Edge Detection", sobel_y)

# Wait for a key press
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()
