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

# Source points
src_points = np.float32([
    [0, 0],
    [cols - 1, 0],
    [0, rows - 1],
    [cols - 1, rows - 1]
])

# Destination points
dst_points = np.float32([
    [0, 0],
    [cols - 1, 0],
    [0, int(0.7 * rows)],
    [cols - 1, int(0.7 * rows)]
])

# Find Homography matrix
M, _ = cv2.findHomography(src_points, dst_points)

# Apply Homography transformation
homography_img = cv2.warpPerspective(img, M, (cols, rows))

# Save result
cv2.imwrite(
    "transformation_using_Homography_Image.jpg",
    homography_img
)

# Display original and transformed images
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformed Image", homography_img)

print("Homography transformation completed!")
print("Press any key to close.")

cv2.waitKey(0)
cv2.destroyAllWindows()
