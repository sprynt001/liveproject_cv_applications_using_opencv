# Import required modules
# Assumes I am using mlcourse conda environment on my local system
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Create a white canvas
def createCanvas(color, nrows=256, ncols=256):
    """Create an array to be used as a canvas for displaying images"""
    
    # What should the size of the array be?
    if type(color) != np.ndarray:
        color = np.array(color)
    color = color.reshape(1,1,color.size)
    canvas = np.repeat(color, nrows, axis=0)
    canvas = np.repeat(canvas, ncols, axis=1)

    return canvas

# Display an image
def displayImage(image):
    """Display image in a new window"""
    # I am currently using Matplotlib.pyplot because cv2.imshow is not 
    # working on my Ubuntu system. I will change this function to use
    # cv2 once I get cv2.imshow working.
    plt.figure()
    plt.imshow(image)
    plt.show()

# Load the color palette
### Your code here
palette = cv2.imread('./color_palette.jpg')

# Create canvas
# Use the createCanvas function
# you have written above
### Your code here
im_width = palette.shape[0]
im_height = palette.shape[1]
canvas = createCanvas([255,255,255], nrows=im_width, ncols=im_height)

# Display the canvas and the 
# color palette
# Use the functions you have 
# written above
### Your code here
displayImage(palette)
displayImage(canvas)
