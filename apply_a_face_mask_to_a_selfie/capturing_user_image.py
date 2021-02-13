"""This script performs the first part of the liveproject:
    
    This script performs the first part of the liveproject:
        * Loads image of face mask and separates alpha channel from image
        * Allow the user to capture an image using OpenCV
"""

# Using Matplotlib for display as OpenCV.show image is currently not
# working on my linux box
import matplotlib.pyplot as plt
import cv2

# Read in face mask, separate alpha from image
face_mask = cv2.imread('./face_mask.png', cv2.IMREAD_UNCHANGED)
face_mask_img = face_mask[:,:,:-1]
face_mask_alpha = face_mask[:,:,-1]

# Get image from webcam
# Code below adapted from an opencv example
print("Press 'q' to select a frame from the webcam")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    webcam_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', webcam_img)
    # If user presses 'q' store the frame and quit the loop
    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# Display images
print("Press any key to quit")
cv2.imshow('face_mask_image', face_mask_img)
cv2.imshow('face_mask_alpha', face_mask_alpha)
cv2.imshow('webcam_image', webcam_img)

# If user presses any key exit
if cv2.waitKey(0):
    cv2.destroyAllWindows()

#plt.subplot(1,2,1)
#plt.imshow(face_mask_img)
#plt.subplot(1,2,2)
#plt.imshow(face_mask_alpha)
#plt.show()
