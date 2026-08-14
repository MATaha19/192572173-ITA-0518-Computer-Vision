import cv2
import numpy as np
from tkinter import Tk, filedialog

# Open file selection window
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

# Read selected image
img = cv2.imread(image_path, 0)

# Check if image was selected
if img is None:
    print("No image selected.")
    exit()

# Sobel X
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Sobel Y
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Combine Sobel X and Y
edges = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# Convert to displayable format
edges = cv2.convertScaleAbs(edges)

# Save output
cv2.imwrite("Edge_detection.jpg", edges)

# Display original and output
cv2.imshow("Original Image", img)
cv2.imshow("Sobel XY Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
