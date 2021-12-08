import cv2
import numpy as np
import random
img = cv2.imread('lena.jpg')
#print(img)
#print(type(img))
#print(img.shape)
#img = np.empty((300, 300, 3), np.uint8) # 28:36
#for row in range(300):
#    for col in range(img.shape[1]):
#        img[row][col]= [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
newImg = img[400:650, 100:500]



cv2.imshow('img',img)
cv2.imshow('newImg',newImg)

cv2.waitKey(0)

# 31:06