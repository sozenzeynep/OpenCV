import cv2
import numpy as np
'''
events = [i for i in dir(cv2) if 'EVENT' in i]
#dir shows all the classes,functions etc
print(events)  #list of all the events
'''

def click_event(event, x,y,flags,param):
# x and y for where we clicked
    if event == cv2.EVENT_LBUTTONDOWN: #ıts mean left click
        print(x,",",y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + "," + str(y)
        cv2.putText(img,strXY,(x,y),font,.5,(255,255,0),2)      #coordinat for where the mouse is
        #org -> koordinat
        cv2.imshow("image",img)

    if event == cv2.EVENT_RBUTTONDOWN: #its mean right click
         blue = img[y,x,0]
         green = img[y,x,1]
         red = img[y,x,2]
         font = cv2.FONT_HERSHEY_SIMPLEX
         strBGR = str(blue) + "," + str(green) + "," +str(red)
         cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)     #BGR channels for image
         #BGR for black img its 0,0,0
         cv2.imshow("image", img)

img = cv2.imread("lena.jpg")
#img = np.zeros((512,512,3),np.uint8)    zeros for blackscreen
cv2.imshow("image",img)

cv2.setMouseCallback("image",click_event)
#Make sure the windows names are all the same
#onmouse -> function

cv2.waitKey(0)
cv2.destroyAllWindows()