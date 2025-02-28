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
#----------------------------------------------------------------------------------------------
# IQR (Interquartile Range), threshold 임계치 & z_score 개념 원래수치 - 평균값/분산 
data =[21,22,23,24,740,1,26,25,290,28,20,19] #740 1 290

print('이상치 제거전:\n',data, '총갯수 ',len(data),'개')

#해결 1] z_score =data -평균값 /분산 zip 함수 (원래 ,z_score)
#해결 2] zip함수 (원래 , z_score)
#해결 3] abs(데이터) <= 임계치는 2~3 변동

#문제 1 평균, 분산, 길이
num_data = np.array(data)
data_mean = num_data.mean()
data_std = num_data.std()
data_len = len(data)

print('평균값 \n', data_mean, '\n분산값 \n', data_std , '\n길이 \n',
      data_len)
#문제 2 z_score = 리스트 컴프리헨젼 응용
z_scores = [(x-data_mean) / data_std for x in data]
print(z_scores , 'z_scoresss')

threshold = 2 #openCV 처리에서 많이 사용하는 은어
IQR = [x for x,z in zip(data,z_scores) if abs(z) <= 0.8]
terminate = [x for x,z in zip(data,z_scores) if abs(z) >= 0.8]

print(IQR, '총갯수', len(IQR), '개')
print(terminate , '이상치 제거값')

#해결 3] 제거된 숫자값 출력

