import cv2

# Input video path
video_path = r"C:\Users\Mohammed Taha\OneDrive\Pictures\video.mp4"

# Output video paths
slow_output = r"C:\Users\Mohammed Taha\OneDrive\Pictures\slow_motion.mp4"
fast_output = r"C:\Users\Mohammed Taha\OneDrive\Pictures\fast_motion.mp4"

# Open video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video!")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Codec
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Create output videos
slow_writer = cv2.VideoWriter(slow_output, fourcc, fps/2, (width, height))
fast_writer = cv2.VideoWriter(fast_output, fourcc, fps*2, (width, height))

print("Processing... Please wait.")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Write the same frame to both videos
    slow_writer.write(frame)
    fast_writer.write(frame)

    # Show processing window
    cv2.imshow("Processing Video", frame)

    # Press ESC to stop early
    if cv2.waitKey(1) == 27:
        break

# Release everything
cap.release()
slow_writer.release()
fast_writer.release()
cv2.destroyAllWindows()

print("\nDone!")
print("Slow Motion Video saved at:")
print(slow_output)

print("\nFast Motion Video saved at:")
print(fast_output)
