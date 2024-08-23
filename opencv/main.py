import cv2 as cv

#Read, Display & Save image

# read image to a variable
image = cv.imread('binary.jpg')  #0 for black and white

#show image on window
# Resize the image to fit the window 
image_resized = cv.resize(image, (600, 800))  # Resize to 800x600 or other appropriate dimensions

#Display - name of window that need to be appeared
#imshow - show image on window
cv.imshow('Display', image_resized) 

#save the image
#cv.imwrite('new.jpg', image_resized)

#waitkey - Delay that is required
cv.waitKey(0) 

#close window if any key is pressed
cv.destroyAllWindows()