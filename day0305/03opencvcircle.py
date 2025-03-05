# import matplotlib
# import matplotlib.pyplot as plt        # 첫번째
# from  matplotlib import pyplot as plt  # 두번째
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

# 음수표기 관리
import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import pandas as pd
import numpy as np
import seaborn as sns 
import time
#--------------------------------------------------------------------------------------------

#OpenCV= Open Source Computer Vision 라이브러리

#pip install opencv-python 설치
#pip list

import cv2
# img = cv2.imread('./images/snow.jpg',cv2.IMREAD_GRAYSCALE)
# img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

title='mouse event'
img = cv2.imread('./images/blank_500.jpg')
cv2.imshow(title,img)






def onMouse(event,x,y,flag,param):
    print(f'좌표 {event},x={x} y={y},flag={flag},param={param}')
    if flag:
        cv2.circle(img,(x,y),20,(255,255,255),-1)
    elif flag & cv2.EVENT_FLAG_ALTKEY:
        cv2.circle(img,(x,y),20,(255,0,0),-1)
    elif flag & cv2.EVENT_FLAG_CTRLKEY:
        cv2.addText(img,'AI',(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,5)
        print(f'실행되나 ?')
    else:
        cv2.circle(img,(x,y),20,(255,255,0),-1)
    cv2.imshow(title,img)
cv2.setMouseCallback(title,onMouse) #화면등록 = show

import sys

if cv2.waitKey(0) &0xFF == 27:
    print('프로그램을 종료합니다.')
    cv2.destroyAllWindows()
    sys.exit()


print()
print()


#순서 마우스 이벤트 함수 호출 담당하는 콜백함수 호출되는 함수명 def onMouse(1,2,3,4,5):
#순서2 ] 마우스 이벤트 왼쪽 마우스 버튼 +  ctrl 레드색 shift 블루색, ctrl+shift 그린색 = cv2.circle 그리기
#순서 3] 마우스 이벤트 함수 호출 담당하는 콜백함수 cv2.setMouseCallback('mouse event',onMouse)
cv2.EVENT_LBUTTONDOWN , cv2.EVENT_FLAG_CTRLKEY , cv2.EVENT_FLAG_SHIFTKEY


'''
처음 수작업으로 원, 텍스트,사각형 좌표 고정값으로 출력 연습 ok
img = cv2.imread('./images/blank_500.jpg')
cv2.circle(img,(55,50),30,(255,0,0),-1)
cv2.putText(img,'suyeon', (100,400),cv2.FONT_HERSHEY_SIMPLEX,2,(0,200,200))
cv2.rectangle(img,(100,300),(300,500),(255,0,0),2)
cv2.recoverPose(img,)
cv2.circle(img,(200,70),30,(255,100,0),-1)
cv2.circle(img,(400,50),30,(180,50,0),-1)
plt.imshow(img)
plt.axis('off')
plt.show()

'''