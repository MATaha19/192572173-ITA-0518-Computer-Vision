import cv2
from tkinter import Tk, filedialog

# Upload / select image
root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

# Read selected image
image = cv2.imread(file_path)

if image is None:
    print("Image not selected or could not be loaded.")
    exit()

# Get image dimensions
width = image.shape[1]
height = image.shape[0]

print("Width:", width)
print("Height:", height)

# Create window
cv2.namedWindow("Original Image")

# Move window to position (100, 100)
cv2.moveWindow("Original Image", 100, 100)

# Display image
cv2.imshow("Original Image", image)

print("Press any key to close.")

cv2.waitKey(0)
cv2.destroyAllWindows()
