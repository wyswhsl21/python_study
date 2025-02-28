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
path ='./data/salaryData.csv'

df= pd.read_csv(path,encoding='cp949')

print(df.info())
#해결 3] null 값 찾는것
print(df.isna().sum()) #null 값 찾는것

#문제 3] null값 대체
df.fillna(df['Age'].mean(),inplace=True)
print(df)
df.fillna(df['Salary'].mean(),inplace=True)
print(df)