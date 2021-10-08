'''Steps  will be following
1.Converting image to grayscale
2. Performing gaussian Blur
3. Applying Canny Edge Detetion
4. Applying segmentation
5. Performing Hoough Trasnform
6. Output '''


import cv2 
import numpy as np
import matplotlib.pyplot as plt

#Reading the image

img=cv2.imread('solidWhiteRight.jpg')
cv2.imshow('Orignal',img)

color_select=np.copy(img)
#Converting to grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale',gray)

#reducing noise in the image
gauss=cv2.GaussianBlur(gray,(7,7),0)

#Canny Edge detection

edge=cv2.Canny(gray,150,255)
cv2.imshow('Canny',edge)

'''
#color selection
red_thresh=200
green_thresh=200
blue_thresh=200

rbg_thresh=[red_thresh,green_thresh,blue_thresh]

thresh=(img[:,:,0]<red_thresh)|(img[:,:,1]<green_thresh)|(img[:,:,2]<blue_thresh)
color_select[thresh]=[0,0,0]

cv2.imshow('thresholding',color_select)
'''

# Segmentation or masking of image

 
    # frame.shape[0] rows of pixels the frame has.
height = edge.shape[0]
width=edge.shape[1]
    # Creates a triangular polygon for the mask defined by three (x, y) coordinates

polygons = np.array([
                            [(120,531), (480, 310), (876, 540)]
                        ])
    # Creates an image filled with zero intensities with the same dimensions as the frame
mask = np.zeros_like(edge)
    # Allows the mask to be filled with values of 1 and the other areas to be filled with values of 0
cv2.fillPoly(mask, polygons, 255)
    # A bitwise and operation between the mask and frame keeps only the triangular area of the frame
segment = cv2.bitwise_and(edge, mask,1)
cv2.imshow('segment',segment)

#cv2.imshow(gray)
# Hough Transformation

new = img.copy()
    

cv2.waitKey(0)