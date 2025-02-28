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
path = './data/Clean_Dataset.csv'
# 해결1] 판다스 df = pd.read_csv(path, encoding='cp949')   행*열 확인
# 해결2] 판다스  열 확인하면 Unnamed: 0 제거 
df = pd.read_csv(path, encoding='cp949')
df.drop(['Unnamed: 0'],axis=1, inplace=True)

print(df)
print()

#해결 3] pd.info()
# print(df.info())
#해결 4] z_score = [컴프레헨젼]


# print(df_zscore)
# 해결 5]
#이상치 평균, 표준편차 , 사용정의 함수
def create_zscore(df,column):
    treshold =2.5
    z_score = (df[column] - df[column].mean()) / df[column].std()
    df_result =  df[abs(z_score) <= treshold]
    return df_result


abs_rst = create_zscore(df,'price')
print(abs_rst,'zscoreeee')
print('이상치 전',df.shape)
print('이상치 후 ', abs_rst.shape)
print('이상치 제거 갯수', len(df) - len(abs_rst))

fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(12,5),sharey=True)
sns.histplot(df, x='price',kde=True,  ax=ax[0])
sns.histplot(abs_rst,x='price', kde=True,  ax=ax[1])  # ax[1]에 그려야 함

plt.show()


