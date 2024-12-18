import cv2 as cv

img = cv.imread("C:\Python\opencv\lena.jpg", 1)   #loads color image since flag is 1.
print(img)

cv.imshow('Display', img)    #Display - display window name
k = cv.waitKey(0)             #Delay

if k == 27:
    cv.destroyAllWindows()       #Destroy the window after time
elif k == ord('s'):
#write image to a file
    cv.imwrite('C:/Python/opencv/copy.png', img)
    cv.destroyAllWindows()