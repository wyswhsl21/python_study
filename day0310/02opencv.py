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
img = cv2.imread('./images/snow.jpg',cv2.IMREAD_GRAYSCALE)
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# plt.imshow(img_rgb)
# plt.title('변환 RGB')
# plt.show()


# 찾아보기 YUV 의미 HSV= Hue(색상), Saturation(채도), Value(명도)

path ='./images/scuba.mp4'
video = cv2.VideoCapture(path)
check,frame = video.read()
print(f'check 값 확인 {check} ') #True
print(f'frame 값 확인 {frame} ') #숫자 형태
cv2.imshow('test',frame) #plt.imshow(img_rgb)

plt.show()
cv2.waitKey()
video.release()

#해결 2] check 변수활용 동영상 play
video = cv2.VideoCapture(path)
num =0
while video.isOpened():
    check,frame = video.read()
    if not check:
        print('scuba 동영상 play 종료되었습니다.')
        break
    else:
        cv2.imshow('test',frame)
        mypath ='./images/my/best_'+str(num) +'.jpg'
        cv2.imwrite(mypath,frame)
        if cv2.waitKey(10) == ord('q'):
            print('영상을 강제 종료합니다')
            break
        num = num+1

video.release() # 메모리 자원을 반환 , 메모리 leak 누수

print()
print()
