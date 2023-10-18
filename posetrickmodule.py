import cv2 as cv
import mediapipe as mp
import time

class Posedetector:

    def __init__(self, mode=False,detectionconf=0.5,trackingconf=0.5,idno=0):
        self.mode = mode
        self.detectionconf=detectionconf
        self.trackingconf=trackingconf

        self.mppose = mp.solutions.pose
        self.pose=self.mppose.Pose()
        self.mpDraw = mp.solutions.drawing_utils
        self.idno = idno


    def findpose(self,img,draw=True):
        #将图片转换为rgb格式
        imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        #当检测到手的坐标时
        if self.results.multi_hand_landmarks:
            #当有多个手对象时,分别提取每一个对象的值,并连接起来
            for poseLms in self.results.multi_pose_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,poseLms,self.mppose.POSE_CONNECTIONS)
        return img


    def findpoint(self,img,draw=True):

        lmlist=[]
        if self.results.multi_pose_landmarks:
            mypose =self.results.multi_pose_landmarks[self.idno]

            for id,lm in enumerate(mypose.landmark):
                # print(id,lm) #landmark一共标记了 21个点，所以id是0~20
                h,w,c=img.shape
                cx,cy= int(lm.x * w),int(lm.y * h) #计算landmark在坐标上的位置（像素单位）

                lmlist.append([id,cx,cy])

                if draw:
                    cv.circle(img,(cx,cy),15,(255,0,255),cv.FILLED)
        else:
            print('the point id is over range')
        #获得21个关节的位置
        return lmlist




def main():
    ##使用摄像头
    cTime = 0
    pTime = 0
    cap = cv.VideoCapture(0)
    idno = 1
    detector = Posedetector(idno=idno)

    while True:
        success, img = cap.read()
        img=detector.findpose(img)
        position=detector.findpoint(img)

        if len(position) >= :
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
