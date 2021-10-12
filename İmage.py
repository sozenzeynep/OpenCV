import cv2

img =cv2.imread("lena.jpg",0)

'''There are three flags:
    1 -> Loads a color image
    0 -> Loads image in grayscale mode
   -1 -> Loads image as such including alpha channel
'''

print(img)

cv2.imshow("Image",img)
#winname = Name of your Window

k= cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
# 27 equals to ESC in binary
#if you press ESC its going to destroy all the windows

elif k == ord('s'):
    cv2.imwrite("lena_copy2.png",img)
    cv2.destroyAllWindows()
#ord() function takes string argument of a single Unicode character and return its integer Unicode code point value.
#if you press s key its going to save image


