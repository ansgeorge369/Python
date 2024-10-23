import cv2 as cv

capture = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')     #refer fourcc

#store the output
output = cv.VideoWriter('C:/Python/opencv/output.avi', fourcc, 20.0, (640,480))   #o/p name, fourcc, fps, size 

print(capture.isOpened())

#capture continiously
while(True):
    ret, frame = capture.read()  #returns true if frame is available frame capture and stores the image
    
    if ret == True:
    
       width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
       height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
    
       print(height)
       print(width)
       
       output.write(frame)
    
       gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
       cv.imshow('Display', gray)
    
    
       if cv.waitKey(1) == ord('q'):
           break
    
    else:   
        break
    
capture.release()
output.release()
cv.destroyAllWindows()