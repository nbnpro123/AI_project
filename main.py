import cv2


img = cv2.imread(r"D:\Proekts\pythonProject\images\1.jpg")
img = cv2.resize(img,(img.shape[1] // 2, img.shape[0] // 2 ))
img = cv2.GaussianBlur(img,(5,5),0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img = cv2.Canny(img, 90, 90)

cv2.imshow('Result',img)
print(img.shape)
cv2.waitKey(0)
