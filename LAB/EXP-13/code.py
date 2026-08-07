import cv2
import numpy as np

# Source points from the camera frame
roi_points = np.array([
    (150, 200),
    (450, 200),
    (550, 500),
    (50, 500)
], dtype=np.float32)

# Target points
target_points = np.array([
    (0, 0),
    (400, 0),
    (400, 600),
    (0, 600)
], dtype=np.float32)

# Calculate perspective transformation matrix
M = cv2.getPerspectiveTransform(roi_points, target_points)

# Open webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Could not access camera.")
        break

    # Apply perspective transformation
    dst = cv2.warpPerspective(frame, M, (400, 600))

    # Display original frame
    cv2.imshow("Original Frame", frame)

    # Display transformed frame
    cv2.imshow("Transformed Frame", dst)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera
cap.release()
cv2.destroyAllWindows()
