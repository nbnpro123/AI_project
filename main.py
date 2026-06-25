import cv2
import numpy as np

# Обработка фото в 2bit разрешении
#img = cv2.imread(r"D:\Proekts\pythonProject\images\1.jpg")
#img = cv2.resize(img,(img.shape[1] // 2, img.shape[0] // 2 ))
#img = cv2.GaussianBlur(img,(5,5),0)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#img = cv2.Canny(img, 70, 70)



#kernel = np.ones((5,5),np.uint8)


#img = cv2.dilate(img, kernel, iterations=1)


#img = cv2.erode(img, kernel, iterations=1)

#cv2.imshow('Result',img)
#print(img.shape)
#cv2.waitKey(0)





# Чёрное фото с фигурами

#photo[100:150, 15:123] = 203, 148, 214

#photo = np.zeros((900, 900, 3), np.uint8)
#cv2.rectangle(photo, (100, 100), (300, 300), (203, 148, 214), 4)
#cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[0], photo.shape[1] // 2), (203, 148, 214), 4)
#cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (103, 1, 1), -1)
#cv2.putText(photo, "test Text", (110 , 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

#cv2.imshow('photo', photo)
#cv2.waitKey(0)


cap = cv2.VideoCapture(r"D:\Proekts\pythonProject\videos\video1.mp4")

while True:
    success, img = cap.read()
    # img = cv2.resize(img,(img.shape[1] // 2, img.shape[0] // 2 ))
    img = cv2.GaussianBlur(img,(5,5),0)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    img = cv2.Canny(img, 100, 100)



    kernel = np.ones((5,5),np.uint8)


    img = cv2.dilate(img, kernel, iterations=1)


    img = cv2.erode(img, kernel, iterations=1)

    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cv2.waitKey(0)



















