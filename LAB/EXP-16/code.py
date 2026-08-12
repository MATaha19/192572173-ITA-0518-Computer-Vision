import cv2

# Read the image
img = cv2.imread(r"C:\Users\Mohammed Taha\OneDrive\Pictures\Chartwork\images (1).jpg", 0)

# Canny Edge Detection
edges = cv2.Canny(img, 100, 200)

# Display original image
cv2.imshow("Original Image", img)

# Display edge detected image
cv2.imshow("Canny Edge Detection", edges)

# Save the output
cv2.imwrite("Edges.jpg", edges)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
