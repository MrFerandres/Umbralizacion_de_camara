import cv2
import numpy as np
import copy

#Iniciamos la camara
cap= cv2.VideoCapture(0)
ret,frame=cap.read()
height, width = frame.shape[0:2]

bg=cv2.imread('Background/back1.jpg')

while(True):
    #Capturamas la camara, cambiamos a escala de grises.

    thresh= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(thresh,127,1,cv2.THRESH_BINARY_INV)

    #mascara=copy.copy(frame*0)
    mascara=copy.copy(bg)
    



    mascara[:,:,0] = frame[:, :, 0] * thresh[:, :]
    mascara[:,:,1] = frame[:, :, 1] * thresh[:, :]
    mascara[:,:,2] = frame[:, :, 2] * thresh[:, :]

    thresh = (thresh - 1) * -1
    mascara[:, :, 0] = mascara[:, :, 0] + bg[:, :, 0] * thresh[:, :]
    mascara[:, :, 1] = mascara[:, :, 1] + bg[:, :, 1] * thresh[:, :]
    mascara[:, :, 2] = mascara[:, :, 2] + bg[:, :, 2] * thresh[:, :]

    cv2.imshow('-Camara-',frame)
    cv2.imshow('-mascara-', mascara)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ret, frame = cap.read()


cap.release()
cv2.destroyAllWindows()



"""   
img = cv2.imread("img\img1.png")

cv2.imshow('--Original--',img)
cv2.waitKey(0)

height, width = img.shape[0:2]
print(height, width)
"""