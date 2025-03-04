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
canny = cv2.Canny(image_gray,lower_threshold,upper_threshold)
plt.imshow(canny,cmap='gray')
print('opencv testing ok 2시 34분')
plt.show()















print()
print()
