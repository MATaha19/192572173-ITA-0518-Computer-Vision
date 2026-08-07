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

# Read image
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
    [50, 50],
    [cols - 51, 50],
    [50, rows - 51],
    [cols - 51, rows - 51]
])

# Construct DLT matrix
A = []

for (x, y), (u, v) in zip(src_points, dst_points):

    A.append([
        -x, -y, -1, 0, 0, 0, x*u, y*u, u
    ])

    A.append([
        0, 0, 0, -x, -y, -1, x*v, y*v, v
    ])

A = np.array(A)

# Solve using Singular Value Decomposition (SVD)
U, S, Vt = np.linalg.svd(A)

# Last row of Vt gives the homography
H = Vt[-1].reshape(3, 3)

# Normalize homography matrix
H = H / H[2, 2]

# Apply transformation
dlt_img = cv2.warpPerspective(img, H, (cols, rows))

# Save result
cv2.imwrite("DLT_Transformed_Image.jpg", dlt_img)

# Display original and transformed images
cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformed Image", dlt_img)

print("Direct Linear Transformation completed!")
print("Press any key to close.")

cv2.waitKey(0)
cv2.destroyAllWindows()
