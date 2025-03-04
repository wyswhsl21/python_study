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
# if img is None:
#     print('이미지 로드 읽기 실패했습니다 \n정확한 파일명 및 경로 및 확장자 꼭 확인하세요 \n')
# else:

# img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) RGB 다시 conversion 시킴
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #변환 과정 필요
plt.imshow(img_rgb) #BGR 인식
plt.title('open cv Test')
plt.axis('off')
plt.show()
#이미지 저장 
img_save = './images/main_new_bluegray.jpg'
cv2.imwrite(img_save,img) #저장경로 , 대상
print('opencv testing ok 11시 33분')
# OpenCV 최대 단점은 컬러가 R레드 G그린 B블루 인식인데 거꾸로 BGR 순으로 인식


# 찾아보기 YUV 의미 HSV= Hue(색상), Saturation(채도), Value(명도)







print()
print()
