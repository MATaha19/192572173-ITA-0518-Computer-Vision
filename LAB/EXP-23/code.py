from PIL import Image, ImageFilter
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

# Open selected image
original = Image.open(image_path)

# Apply unsharp masking
sharpened = original.filter(
    ImageFilter.UnsharpMask(
        radius=3,
        percent=200,
        threshold=5
    )
)

# Display original and sharpened images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(sharpened)
plt.title("Sharpened Image - Unsharp Masking")
plt.axis("off")

plt.tight_layout()
plt.show()

print("Unsharp masking completed successfully.")
