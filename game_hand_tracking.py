import cv2
import mediapipe as mp
import time
import hand_tracking_module as htm
#getting hand tracking as module and running it
pTime=0
cTime=0
cap=cv2.VideoCapture(0)
detector=htm.handDetector()
while True:
    sucess,img=cap.read()
    img =detector.find_hands(img)
    lmlist=detector.findPosition(img)
    if len(lmlist)!=0:
        print(lmlist[4])
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img, str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
    cv2.imshow("Image", img)
    # print(sucess)
    cv2.waitKey(1)