import cv2

cap = cv2.VideoCapture(0)
print("Width:",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height:",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,1280)
cap.set(4,720)
#camera will only set for resolution which is available for it
'''
    3 for Width 
    4 for Heigth
'''
print("New Width:",cap.get(3))
print("New Height:",cap.get(4))
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        cv2.imshow("My Frame",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()