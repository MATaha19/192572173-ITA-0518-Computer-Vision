import cv2
import numpy as np
from tkinter import Tk, filedialog

# Select / upload image
root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

# Read selected image
img = cv2.imread(file_path)

if img is None:
    print("Image not selected or could not be loaded.")
    exit()

# Get image dimensions
rows, cols = img.shape[:2]

# Affine transformation matrix
M = np.float32([
    [1, 0, 100],
    [0, 1, 50]
])

# Apply affine transformation
affine_img = cv2.warpAffine(img, M, (cols, rows))

# Save transformed image
cv2.imwrite("Affine_Transformed.jpg", affine_img)

# Display original and transformed images
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed Image", affine_img)

print("Affine transformation completed!")
print("Press any key to close.")

cv2.waitKey(0)
cv2.destroyAllWindows()
