"""Script to detect faces in webcam

"""

import sys
import cv2

# Load haar cascade
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

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
fpath = "./webcam_face.avi"
writer = cv2.VideoWriter(fpath, fourcc, frame_rate, (width, height))

print("Press 'q' to stop webcam grab.")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces and draw on frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)

    # Write frame to output and display
    writer.write(frame) 

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release all resources
cap.release()
writer.release()
cv2.destroyAllWindows()

print("Saved video stream to {fpath}")
