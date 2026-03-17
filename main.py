import cv2
import torch
import numpy as np

# Print PyTorch version to confirm the deep learning library is ready
print(f"PyTorch Version: {torch.__version__}")

# Initialize the default webcam (0 is usually the built-in Mac camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam. Please check your Mac's privacy settings.")
    exit()

print("Webcam successfully launched! Press 'q' in the video window to quit.")

while True:
    # Read the video frame by frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Display the resulting frame in a window
    cv2.imshow('Robotic Sorting - Camera Test', frame)

    # Wait for 1 millisecond, and check if the 'q' key is pressed to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and close windows
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
