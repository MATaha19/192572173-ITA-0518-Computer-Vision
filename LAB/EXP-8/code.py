import cv2

image = cv2.imread(r"C:\Users\Mohammed Taha\OneDrive\Pictures\Chartwork\images (4).jpg")

if image is None:
    print("Image not found!")
    exit()

# Resize original image to fit the screen
image = cv2.resize(image, (500, 350))

# Create resized versions
bigger_image = cv2.resize(image, (650, 455))
smaller_image = cv2.resize(image, (350, 245))

cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger_image)
cv2.imshow("Smaller Image", smaller_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
