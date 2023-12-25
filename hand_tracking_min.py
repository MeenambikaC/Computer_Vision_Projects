import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)

while True:
    sucess,img=cap.read()


    cv2.imshow("Image", img)
    print(sucess)
    cv2.waitKey(1000)
