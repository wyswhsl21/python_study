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
# OpenCV = Open Source Computer Vision 라이브러리 
# pip install opencv-python 설치

# 06HSV.py문서 
import cv2
img = cv2.imread('./images/corgi.jpg')
plt.title('BGR 원본 이미지 ok')
plt.imshow(img) #BGR원본
plt.show()

# img = cv2.imread('./images/main.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
plt.title('사람이 가장 정확하게 판별하는 컬러 RGB변환한  이미지 ok')
plt.imshow(img_rgb) #RGB변환
plt.show()

# img = cv2.imread('./images/main.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #HSV적용 HSV = Hue(색상), Saturation(채도), Value(명도)
plt.title('COLOR_BGR2HSV적용  이미지 ok')
plt.imshow(hsv_img ) #BGR2HSV변환
plt.show()

# img = cv2.imread('./images/main.jpg')
yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV) #YUV적용
plt.title('COLOR_BGR2YUV적용  이미지 ok')
plt.imshow(yuv_img) #BGR2YUV변환
plt.show()



# cv2.imshow('H 적용', hsv_img[ : , : , 0] )  #완전 어두운컬러 
# cv2.imshow('S 적용', hsv_img[ : , : , 1] )  #어두운컬러이기는 하지만 형태구별 선명함
# cv2.imshow('V 적용', hsv_img[ : , : , 2] )  #회색이면서 완전한 형태구별 가능함
plt.show()
cv2.waitKey() #키값의 입력받겠다는 의미 

# yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV) #YUV적용
# cv2.imshow('Y 적용', yuv_img[ : , : , 0] ) #회색가까운 컬러적용 grayscale동일하게 적용
# cv2.imshow('U 적용', yuv_img[ : , : , 1] ) #Blue
# cv2.imshow('V 적용', yuv_img[ : , : , 2] ) #Red
# plt.show()
# cv2.waitKey() #키값의 입력받겠다는 의미 
# # cv2.destroyAllWindows()


# # HSV = Hue(색상), Saturation(채도), Value(명도)
# # YUV = 휘도(Luminance흑백, Y)와 색차(Chrominance, U=blue, V=red) 신호
print('opencv testing ok 21시 05분 ')













print()
print()
