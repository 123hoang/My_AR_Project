import cv2 as cv
import numpy as np
#Read Image from file load from directory
img1 = cv.imread("image/saigon.jpg")
#Size height, wweight
print("The characteristic of "+"image1 is ")
print(img1.shape)
#Size of memory
print("The size of the img1 is")
print(img1.size)

#Read Image from file load from directory
img2 = cv.imread("image/Van-gogh.jpg")
#Size height, wweight
print("The characteristic of "+"image2 is ")
print(img2.shape)
#Size of memory
print("The size of the img1 is")
print(img2.size)
