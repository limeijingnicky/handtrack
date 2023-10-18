import cv2 as cv
import mediapipe as mp
import time

##使用摄像头
cap = cv.VideoCapture(0)

mphands = mp.solutions.hands
hands=mphands.Hands()
mpDraw = mp.solutions.drawing_utils
cTime=0
pTime=0
# 初始化一个变量用于控制循环
stop_button = 1

while stop_button == 1 :
    success,img = cap.read()

    #将图片转换为rgb格式
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    #当检测到手的坐标时
    if results.multi_hand_landmarks:
        #当有多个手对象时,分别提取每一个对象的值,并连接起来
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm) #landmark一共标记了 21个点，所以id是0~20
                h,w,c=img.shape
                cx,cy= int(lm.x * w),int(lm.y * h) #计算landmark在坐标上的位置（像素单位）
                # print(id,cx,cy)

                #标记出id为0的点的位置
                if id==0:
                    cv.circle(img,(cx,cy),20,(255,0,255),cv.FILLED)
                mpDraw.draw_landmarks(img,handLms,mphands.HAND_CONNECTIONS)

    #计算帧
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    #将帧速标记在视频图片上
    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    cv.imshow("image",img)

    # 使用 cv.waitKey() 来等待用户按键输入
    key = cv.waitKey(1)

#     # 如果用户按下键盘上的数字键 "0"，则停止循环
#     if key == ord('0'):
#         stop_button = 0
#
# # 释放摄像头资源和关闭窗口
# cap.release()
# cv.destroyAllWindows()



