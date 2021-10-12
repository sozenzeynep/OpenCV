#Flintstones Style Object Detection
import cv2
import numpy as np

cam = cv2.VideoCapture(0);

while(cam.isOpened()):
    ret, frame = cam.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    nesne = cv2.imread("pen.jpg",0)

    w,h = nesne.shape

    res = cv2.matchTemplate(gray_frame,nesne,cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    loc = np.where(res>threshold)
    for n in zip(*loc[::-1]):
        cv2.rectangle(frame,n,(n[0]+h,n[1]+w),(0,255,0),2)
        cv2.putText(frame,"Pen",(n[0]+10,n[1]+10),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0))

    cv2.imshow("Frame",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cam.release()
cv2.destroyAllWindows()
