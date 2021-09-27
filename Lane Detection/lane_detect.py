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
gauss=cv2.GaussianBlur(gray,(5,5),0)

#Canny Edge detection

edge=cv2.Canny(gray,50,150)
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


#cv2.imshow(gray)



cv2.waitKey(0)