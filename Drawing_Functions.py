import cv2

img = cv2.imread("lena.jpg",1)
img = cv2.line(img,(0,0),(255,255),(0,120,255),5) #bgr                                 #Drawing Line
img = cv2.arrowedLine(img,(0,255),(255,255),(0,0,255),5)                             #Drawing Arrow
img = cv2.rectangle(img,(384,0),(510,128),(100,0,255),5)                               #Drawing Rectangle
'''
topleft => pt1
lowerright => pt2
'''
img = cv2.circle(img,(447,63),63,(0,255,0),-1)                                       #Drawing Circle
#thickness = -1  -> fill rectangle

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,"Lena",(10,500),font,4,(158,124,75),10,cv2.LINE_AA)
#org->starting point

cv2.imshow("Lena",img)
cv2.waitKey(0)
cv2.destroyAllWindows()