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
img = cv2.imread('./images/snow.jpg')
print(img)
plt.title('BGR 원본 이미지')
plt.imshow(img)
plt.show()
print()
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
print(img_rgb,'snow 변환한 정보')
print()
print()

plt.title('RGB 변환한 이미지 ok')
plt.imshow(img_rgb)
plt.show()

# cv2.destroyAllWindows()

# HSV= Hue(색상), Saturation(채도), Value(명도)
# YUV는 휘도(Luminance흑백, Y)와 색차(Chrominance, U=blue, V=red) 신호
print('opencv testing ok 1시 25분 ')






print()
print()
