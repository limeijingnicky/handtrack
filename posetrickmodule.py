import cv2 as cv
import mediapipe as mp
import time

class Posedetector:

    def __init__(self, mode=False,maxpose=2,detectionconf=0.5,trackingconf=0.5,poseno=0):
        self.mode = mode
        self.maxhands=maxpose
        self.detectionconf=detectionconf
        self.trackingconf=trackingconf

        self.mphands = mp.solutions.hands
        self.hands=self.mphands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.poseno= poseno

    def findpose(self,img,draw=True):
        #将图片转换为rgb格式
        imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        #当检测到手的坐标时
        if self.results.multi_hand_landmarks:
            #当有多个手对象时,分别提取每一个对象的值,并连接起来
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLms,self.mphands.HAND_CONNECTIONS)
        return img


    def findposition(self,img,draw=True):

        lmlist=[]
        if self.results.multi_hand_landmarks:
            myhand =self.results.multi_hand_landmarks[self.handno]

            for id,lm in enumerate(myhand.landmark):
                # print(id,lm) #landmark一共标记了 21个点，所以id是0~20
                h,w,c=img.shape
                cx,cy= int(lm.x * w),int(lm.y * h) #计算landmark在坐标上的位置（像素单位）

                lmlist.append([id,cx,cy])

                if draw:
                    cv.circle(img,(cx,cy),15,(255,0,255),cv.FILLED)
        else:
            print('the handno is over range')
        #获得21个关节的位置
        return lmlist




def main():
    ##使用摄像头
    cTime = 0
    pTime = 0
    cap = cv.VideoCapture(0)
    handno=1
    detector=Handdetector(handno=handno)

    while True:
        success, img = cap.read()
        img=detector.findhands(img)
        position=detector.findposition(img)

        if len(position) >= handno:
            #得到第0个关节的位置
            print(position)

        # 计算帧
        cTime  = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # 将帧速标记在视频图片上
        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv.imshow("image", img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()
