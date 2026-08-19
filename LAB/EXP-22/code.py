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

# Read the selected image
image = cv2.imread(image_path)

if image is None:
    print("No image selected or image could not be loaded.")
    exit()

# Laplacian mask with positive center coefficient
kernel = np.array([
    [0, 1, 0],
    [1, -8, 1],
    [0, 1, 0]
])

# Apply the mask
sharpened = cv2.filter2D(image, -1, kernel)

# Display images
cv2.imshow("Original", image)
cv2.imshow("Sharpened", sharpened)

print("Press any key to close the images.")

cv2.waitKey(0)
cv2.destroyAllWindows()
