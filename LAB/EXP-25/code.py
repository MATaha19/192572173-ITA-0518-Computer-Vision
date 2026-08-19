import cv2
import numpy as np
from tkinter import Tk, filedialog
import matplotlib.pyplot as plt

# Open file selection window
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

if not image_path:
    print("No image selected.")
    exit()

# Read selected image
image = cv2.imread(image_path)

if image is None:
    print("Image could not be loaded.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate gradient in X direction
gradient_x = cv2.Sobel(
    gray,
    ddepth=cv2.CV_64F,
    dx=1,
    dy=0,
    ksize=3
)

# Calculate gradient in Y direction
gradient_y = cv2.Sobel(
    gray,
    ddepth=cv2.CV_64F,
    dx=0,
    dy=1,
    ksize=3
)

# Gradient masking
gradient = cv2.subtract(gradient_x, gradient_y)

# Convert result for proper display
gradient_display = cv2.convertScaleAbs(gradient)

# Save output
cv2.imwrite("sharpened_image3.jpg", gradient_display)

# Convert original image from BGR to RGB
original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display original and output
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gradient_display, cmap="gray")
plt.title("Gradient Masked Image")
plt.axis("off")

plt.tight_layout()
plt.show()

print("Gradient masking completed successfully.")
