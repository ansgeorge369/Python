import numpy as np
import cv2

#img = cv2.imread("C:\Python\opencv\lena.jpg", 1)
img = np.zeros([512, 512, 3], np.uint8)

#what need to be processed, startinga nd ending coordinates in tuples, color in BGR format, thickeness
img = cv2.line(img, (0, 0), (255, 255), (0, 255, 0), 5)  
img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 255, 0), 5)

#what image needs to be processed, upper left coordinates, lower right coordinates, color, thickness
img = cv2.rectangle(img, (384,0), (510,128), (0,255,0), 5)  #-1 shape will be filled with the specified color

img = cv2.circle(img, (447,63), 63, (0, 255, 0), -1)  # centre and radius in case of circle
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'OpenCV', (10,500), font, 2, (255,255,255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()