import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = width, height

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('photos/flower.jpg')
cv.imshow('flower', img)
cv.imshow('flower_resize', rescaleFrame(img))

cv.waitKey(0)