#Shows Current Date and Time
import cv2
import datetime

cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_DUPLEX
        date_t = str(datetime.datetime.now())   #Gives you current Date and Time
        frame =cv2.putText(frame,date_t,(10,50),font,1,(0,255,178),2,cv2.LINE_AA)
        cv2.imshow("My Frame",frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()