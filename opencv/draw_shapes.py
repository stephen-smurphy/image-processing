import cv2 as cv
import numpy as np

#create blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)


#Paint Image a certain colour (cyan)
#blank[:] = 255, 255, 0
#cv.imshow('Painted', blank)

#Draw a rectangle
#cv.rectangle(blank, (0,0), (250,250), (0,255,0), 2)
#cv.imshow('Rectangle', blank)

#Draw a circle
#cv.circle(blank, (250,250), radius=40, color=(0,0,255), thickness=-1)
#cv.imshow('Circle', blank)

#Draw a line
#cv.line(blank, (100,100), (200,200), color=(255,0,0))
#cv.imshow('Line', blank)

#Write text
cv.putText(blank, 'Hello', (250,250), color=(0,255,0), fontFace=cv.FONT_HERSHEY_COMPLEX, fontScale=1.0)
cv.imshow('Text', blank)


cv.waitKey(0)