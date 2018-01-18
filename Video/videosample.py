import numpy as np
import cv2

img = cv2.imread('1.pgm',cv2.IMREAD_COLOR)
cv2.rectangle(img,(15,25),(200,150),(0,0,255),15)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
