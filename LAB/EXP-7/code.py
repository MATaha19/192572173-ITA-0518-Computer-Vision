import cv2

video_path = r"C:\Users\Mohammed Taha\OneDrive\Pictures\video.mp4"

print("Press S for Slow Motion")
print("Press F for Fast Motion")

choice = input("Enter your choice (S/F): ").upper()

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video.")
    exit()

if choice == "S":
    delay = 100      # Slow
elif choice == "F":
    delay = 5        # Fast
else:
    delay = 30       # Normal

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video Playback", frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
