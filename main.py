import cv2


img = cv2.imread(r"D:\Proekts\pythonProject\images\1.jpg")
img = cv2.resize(img,(img.shape[1] // 2, img.shape[0] // 2 ))

cv2.imshow('Result',img)
print(img.shape)
cv2.waitKey(0)
