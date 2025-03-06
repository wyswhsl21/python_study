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
print('')

#np 이용하여 이미지 배열 만드는 함수 (450,350) 크기의 3채널 BGR 이미지 생성
#모든 픽셀 값을 0으로 설정 -> 검은색 배경
# 8비트 정수형 데이터 사용
img = np.full((450,350,3),0,dtype=np.uint8) 
cv2.circle(img,(100,100),70,(0,255,0),-1) # 좌표, 원의 반지름, 색깔, 채우기 음수값인 경우 내부를 채움
cv2.putText(img,'summer',(100,300),cv2.FONT_HERSHEY_TRIPLEX,2,(0,0,255))
cv2.rectangle(img,(100,350),(300,450),(255,0,0),2) #왼쪽 위 좌표 , 오른쪽 아래 좌표, 파란색 BGR, 선 두께

print(img)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()


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