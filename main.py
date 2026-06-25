import cv2
import numpy as np

# # Обработка фото в 2bit разрешении
# img = cv2.imread(r"D:\Proekts\pythonProject\images\1.jpg")
# img = cv2.resize(img,(img.shape[1] // 2, img.shape[0] // 2 ))
# img = cv2.GaussianBlur(img,(5,5),0)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# img = cv2.Canny(img, 70, 70)
#
#
#
# kernel = np.ones((5,5),np.uint8)
#
#
# img = cv2.dilate(img, kernel, iterations=1)
#
#
# img = cv2.erode(img, kernel, iterations=1)
#
# cv2.imshow('Result',img)
# print(img.shape)
# cv2.waitKey(0)





# #Чёрное фото с фигурами
#
#
# photo = np.zeros((900, 900, 3), np.uint8)
# cv2.rectangle(photo, (100, 100), (300, 300), (203, 148, 214), 4)
# cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[0], photo.shape[1] // 2), (203, 148, 214), 4)
# cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (103, 1, 1), -1)
# cv2.putText(photo, "test Text", (110 , 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#
# cv2.imshow('photo', photo)
# cv2.waitKey(0)



# # Подготовка видео к анализу
# cap = cv2.VideoCapture(r"D:\Proekts\pythonProject\videos\video1.mp4")
#
# while True:
#     success, img = cap.read()
#     # img = cv2.resize(img,(img.shape[1] // 2, img.shape[0] // 2 ))
#     img = cv2.GaussianBlur(img,(5,5),0)
#     img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
#     img = cv2.Canny(img, 100, 100)
#
#
#
#     kernel = np.ones((5,5),np.uint8)
#
#
#     img = cv2.dilate(img, kernel, iterations=1)
#
#
#     img = cv2.erode(img, kernel, iterations=1)
#
#     cv2.imshow('Result',img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#
#
# cv2.waitKey(0)



img = cv2.imread(r"D:\Proekts\pythonProject\images\1.jpg")
img = cv2.resize(img,(img.shape[1] // 2, img.shape[0] // 2 ))
# img = cv2.flip(img, 1)


def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = (width // 2, height // 2)

    mat = cv2.getRotationMatrix2D(point, angle, 1.0)
    return cv2.warpAffine(img_param, mat, (width, height))
# img = rotate(img, 90)

def transform(img_param, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))

img = transform(img, 30, 200)


cv2.imshow("Image", img)
cv2.waitKey(0)

















