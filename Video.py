import cv2
cam = cv2.VideoCapture(0);
'''
    0 is default
    1 is USB 
    video.avi is exist video
'''

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))
#cam.set(3,300) #3 is Width
#cam.set(4,300) #4 is Height

while(cam.isOpened()): #isOpened()= T or F
    ret, frame = cam.read()  # ret equals to T(if frame is available) or F
    if ret == True:
        print(cam.get(cv2.CAP_PROP_FRAME_WIDTH)) #gives you width and height
        print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
        bolge = frame[0:200,0:200]
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("My Frame",frame)
        cv2.imshow('Gray Frame',gray)
        cv2.imshow("Little Frame",bolge)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cam.release() #camera is free
out.release() #record is free
cv2.destroyAllWindows()

