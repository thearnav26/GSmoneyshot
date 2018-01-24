import cv2 
import numpy as np
import os

path='test1/'

#Appends all the absolute paths in the list image_paths 
image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('2.pgm')]

#initializing a base_image over which other images will be superimposed
base_image=cv2.imread('8.pgm')

#resizing the base image so it matches the size of the database pics (113(rows),97(columns))
base_image=cv2.resize(base_image,(97,113))

#cv2.imshow('lol',base_image) //for testing purposes

for pics in image_paths:
	im=cv2.imread(os.path.expanduser(pics))
	im=cv2.resize(im,(97,113))
	#to check how many times the im is actually working without any error	
	print im.shape
	#to check how many times the base_image is actually working without any error
	print base_image.shape
	base_image=cv2.addWeighted(base_image,0.5,im,0.5,0)
	base_image=cv2.resize(base_image,(97,113))

cv2.imshow('compiledimg.jpg',base_image)

k = cv2.waitKey(0) & 0xFF
if k == 27:         
    cv2.destroyAllWindows()

elif k == ord('s'): 
    cv2.imwrite('compiledimg.jpg',base_image)
    cv2.destroyAllWindows()





