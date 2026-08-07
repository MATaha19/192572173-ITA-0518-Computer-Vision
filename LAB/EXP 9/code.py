import cv2
from tkinter import Tk, filedialog

# Select image
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
    print("Image could not be loaded.")
    exit()

# Rotate clockwise
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Save rotated image
cv2.imwrite("rotated_image.jpg", rotated_img)

# Display original image
cv2.imshow("Original Image", img)

# Display rotated image
cv2.imshow("Rotated Image", rotated_img)

print("Image rotated successfully!")
print("Press any key to close the windows.")

# Keep both windows open
cv2.waitKey(0)
cv2.destroyAllWindows()
