"""Script to detect eyes in image with haar cascade & hough circle transform

"""

import os
import cv2
from argparse import ArgumentParser

parser = ArgumentParser("Detecting eyes in images using haar cascades " + \
                        "and hough circle transform")
parser.add_argument("-i", "--input-path", required=True,
                    help="path to image to process")
parser.add_argument("-o", "--output-path", default=None,
                    help="path to save image with bounding boxes " + \
                         "if not supplied appends '_hough_eyes' to " +\
                         "input file name")

args = parser.parse_args()

input_path = args.input_path
output_path = args.output_path

image = cv2.imread(input_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')
eyes = eye_cascade.detectMultiScale(gray)

# Blur gray image for hough processing
gray = cv2.medianBlur(gray, 5)

for (x,y,w,h) in eyes:
    # Draw bounding box around eye
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 2)
    # For each subregion detect the circle around the eyes
    roi_gray = gray[y:y+h, x:x+w]

    # Compute the min and max radii using smallest bounding box dimension
    min_radius = int(min(w, h)/12)
    max_radius = min_radius * 4
    circles = cv2.HoughCircles(roi_gray, cv2.HOUGH_GRADIENT, 1, 200,
                               param1=200, param2=20,
                               minRadius=min_radius, maxRadius=max_radius)
    if circles is not None:
        for (cx,cy,r) in circles[0,:]:
            ex = int(x + cx)
            ey = int(y + cy)
            r = int(round(r))
            cv2.circle(image, (ex,ey), r, (0,255,0), 2)
        

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the output to file
if output_path == None:
    dirname, fname = os.path.split(input_path)
    fbase, fext = os.path.splitext(fname)
    output_path = os.path.join(dirname, fbase+"_hough_eyes"+fext)
cv2.imwrite(output_path, image)
print(f"Written processed image to {output_path}")
