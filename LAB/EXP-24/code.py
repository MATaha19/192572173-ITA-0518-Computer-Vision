import cv2
import numpy as np
from tkinter import Tk, filedialog
import matplotlib.pyplot as plt


def high_boost_filter(image, boost_factor):
    kernel_size = 3

    # Create averaging kernel
    kernel = np.ones(
        (kernel_size, kernel_size),
        dtype=np.float32
    ) / (kernel_size ** 2)

    # Create blurred image
    blur_image = cv2.filter2D(image, -1, kernel)

    # High-boost masking
    mask = image + (image - blur_image) * boost_factor

    # Keep pixel values within valid range
    mask = np.clip(mask, 0, 255).astype(np.uint8)

    return mask


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

# Apply High-Boost Mask
sharpened_image = high_boost_filter(image, 1.5)

# Convert BGR to RGB for Matplotlib
original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
sharpened_rgb = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB)

# Display Original and Output
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(sharpened_rgb)
plt.title("High-Boost Sharpened Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("sharpened_image.jpg", sharpened_image)

print("High-Boost sharpening completed successfully.")
