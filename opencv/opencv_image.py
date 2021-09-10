import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile('photos/flower.jpg'))

cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("flower.png", img)
