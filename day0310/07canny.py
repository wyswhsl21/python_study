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

# 07canny.py문서 
import cv2
img = cv2.imread('./images/img_mountains_wide.jpg')
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.title('BGR 원본 이미지 ok')
plt.imshow(img_rgb) #BGR원본
plt.show()

# img = cv2.imread('./images/main.jpg')
image_gray = cv2.imread('./images/img_mountains_wide.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(image_gray)
plt.show()
median_test =np.median(image_gray)
lower_threshold = int(max(10,(1.0-0.22) * median_test))
upper_threshold = int(min(200,(1.0+0.22) * median_test))
#구분 = 경계 = 임계치 = threshold max(0,~~) , min(255,~~)
#경계를 감지하는 알고리즘. 픽셀 값이 급격하게 변화하는 부분을 의미함.
canny = cv2.Canny(image_gray,lower_threshold,upper_threshold)
plt.imshow(canny,cmap='gray')
print('opencv testing ok 2시 34분')
plt.show()

'''
Canny 엣지 검출 과정
1. 노이즈 제거 
cv2.GaussianBlur() 사용해 이미지 노이즈 줄여 불필요한 작은 엣지 제거
2. 기울기 계산
sobel 필터를 이용해 각 픽셀의 밝기 변화율을 계산
3.비최대 억제
너무 두껍게 검출된 엣지를 얇게 만들고 엣지 중심 부분만 남기고 주변 제거
4. 이중 임계값 
두개의 임계값을 사용하여 엣지 결정
강한 엣지는 유지하고 약한 엣지는 강한엣지와 연결될때만 유지

임계값 조절

cv2.Canny(img, 50, 150): 엣지가 많이 검출됨 (예민함)
cv2.Canny(img, 100, 200): 일반적인 설정 (균형적)
cv2.Canny(img, 150, 250): 엣지가 적게 검출됨 (정확하지만 일부 누락 가능)

'''













print()
print()
