import cv2
import numpy as np
from tkinter import Tk, filedialog

# Open image selection window
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

# Read selected image
img = cv2.imread(image_path)

# Check if image was selected
if img is None:
    print("No image selected.")
    exit()

# Laplacian sharpening mask
kernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

# Apply sharpening mask
sharpened = cv2.filter2D(img, -1, kernel)

# Save output
cv2.imwrite("Sharpened_Image.jpg", sharpened)

# Display original and output
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
