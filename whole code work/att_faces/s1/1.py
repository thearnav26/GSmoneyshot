import cv2
import numpy as np

img1=cv2.imread('1.pgm')
img2=cv2.imread('2.pgm')
img3=cv2.imread('3.pgm')
img4=cv2.imread('4.pgm')
img5=cv2.imread('5.pgm')
img6=cv2.imread('6.pgm')
img7=cv2.imread('7.pgm')
img9=cv2.imread('9.pgm')
img10=cv2.imread('10.pgm')

#dst=cv2.addWeighted(img1,0.5,img2,0.5,img3,0.5,img4,0.5,img5,0.5,img6,0.5,img7,0.5,img9,0.5,img10,0.5,0)

dst=cv2.addWeighted(img1,0.5,img2,0.5,0)

cv2.imshow('faces',dst)
k = cv2.waitKey(0)
if k == 27: 
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('new.pgm',dst)
    cv2.destroyAllWindows()
