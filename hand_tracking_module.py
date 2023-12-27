import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self,mode=False,max_Hands=2,model_complexity=1,detectionCon=0.5,trackCon=0.5):
        self.mode=mode,
        self.max_Hands=max_Hands
        self.model_complexity=model_complexity
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,self.max_Hands,self.model_complexity,self.detectionCon,self.trackCon)# can support upto 2 hands 
        self.mpDraw=mp.solutions.drawing_utils

    def find_hands(self,img,draw=True):

        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #hands only supports RGB
        self.results=self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks) #prints landmark if there is a hand

        #if there are multiple hands
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS) #HAND_CONNECTIONS joins the points
        return img
    def findPosition(self,img,handNo=0,draw=True):#landmark of hand

        lmList=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):
                # print(id,lm) #location should given in pixels
                height,width,channel=img.shape
                cx,cy=int(lm.x*width),int(lm.y*height)
                # print(id, cx,cy) #given in pixel
                # print(channel)
                lmList.append([id,cx,cy])
                if draw and id==0:
                    cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)
                
        return lmList        


 


def main():
    pTime=0
    cTime=0
    cap=cv2.VideoCapture(0)
    detector=handDetector()
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
    
    
if __name__=="__main__":
    main()
