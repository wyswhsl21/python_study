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
img = cv2.imread('./images/blank_500.jpg')
img = np.full((450,350,3),0,dtype=np.uint8)
cv2.circle(img,(100,100),70,(0,255,0),-1)
cv2.putText(img,'summer',(100,300),cv2.FONT_HERSHEY_TRIPLEX,2,(0,0,255))
cv2.rectangle(img,(100,350),(300,450),(255,0,0),2)

print(img)
plt.imshow(img)
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