"""Module with functions and script to stream webcam data to a video file

"""

import sys
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Get dimensions of the frames
ret, frame = cap.read()
if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    sys.exit(-1)
height, width = frame.shape[:2]

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
frame_rate = 20.0
fpath = "./webcam.avi"
writer = cv2.VideoWriter(fpath, fourcc, frame_rate, (width, height))

print("Press 'q' to stop webcam grab.")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    writer.write(frame) 

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release all resources
cap.release()
writer.release()
cv2.destroyAllWindows()

print("Saved video stream to {fpath}")
