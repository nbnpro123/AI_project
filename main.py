import cv2
import numpy as np

#img = cv2.imread(r"D:\Proekts\pythonProject\images\1.jpg")
#img = cv2.resize(img,(img.shape[1] // 2, img.shape[0] // 2 ))
#img = cv2.GaussianBlur(img,(5,5),0)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
#img = cv2.Canny(img, 70, 70)
#
#
#
#kernel = np.ones((5,5),np.uint8)
#
#
#img = cv2.dilate(img, kernel, iterations=1)
#
#
#img = cv2.erode(img, kernel, iterations=1)
#
#cv2.imshow('Result',img)
#print(img.shape)
#cv2.waitKey(0)

photo = np.zeros((900, 900, 3), np.uint8)

#photo[100:150, 15:123] = 203, 148, 214



cv2.rectangle(photo, (100, 100), (300, 300), (203, 148, 214), 4)

cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[0], photo.shape[1] // 2), (203, 148, 214), 4)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (103, 1, 1), -1)


cv2.imshow('photo', photo)
cv2.waitKey(0)
