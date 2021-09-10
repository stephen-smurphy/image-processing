import cv2 as cv
import numpy as np

img = cv.imread('photos/flower.jpg')
cv.imshow('Flower', img)

#shows colour intensity
b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

#To show actual colour of each channel
blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue colour', blue)
cv.imshow('Green colour', green)
cv.imshow('Red colour', red)

cv.waitKey(0)