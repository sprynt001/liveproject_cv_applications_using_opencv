"""Script to detect eyes in images using haar cascades

"""

import cv2
from argparse import ArgumentParser

parser = ArgumentParser("Detecting eyes in images using haar cascades")
parser.add_argument("-i", "--input-path", required=True,
                    help="path to image to process")

args = parser.parse_args()

input_path = args.input_path

image = cv2.imread(input_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')
eyes = eye_cascade.detectMultiScale(gray)

for (x,y,w,h) in eyes:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 2)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
