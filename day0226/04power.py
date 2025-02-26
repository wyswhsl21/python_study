import matplotlib
import matplotlib.pyplot as plt        # 첫번째
from  matplotlib import pyplot as plt  # 두번째
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc
import seaborn as sns
# 음수표기 관리
import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import pandas as pd
import numpy as np
import time

# --------------------------------------------------------------------------------------
path ='./data/남북한발전전력량.xlsx'
df = pd.read_excel(path,engine='openpyxl')
print(df)
df_ns = df.loc[5:7]
#해결 2] 전력량 (억㎾h) 열 컬럼 삭제 drop 
df_ns.drop('전력량 (억㎾h)',axis='columns',inplace=True)
print(df_ns)
#해결 3] '발전 전력별' 필드 숫자 index대체 
df_ns.set_index('발전 전력별',inplace=True)
print('- ' * 45)
print(df_ns)
#해결 4] 년도를 행으로 합계, 수력 , 화력을 열컬럼 대체
df_ns = df_ns.T
print('- ' * 45)
print(df_ns)
#해결 5] 현재년도 - 전년도 금액 빼서 사용량 증감인지 감소인지





#해결 1] north 수력 화력 필드를 그래프 하나에 표시
#해결 2] 열을 행으로 전환 T 사용
#해결 3] 년별 차이 2024년 900 2023년 950 2024년 800 

'''
처음실습한 예제 

path ='./data/남북한발전전력량.xlsx'
df = pd.read_excel(path,engine='openpyxl')
# print(df)
df_ns = df.iloc[[0,5],2:]
print(df_ns)
df_ns.index = ['South','North']
# df_ns.columns = df_ns.columns.map(int)

# print(df_ns.columns)
print()
# plt.figure(figsize=(16,7))
# df_ns.plot()
# plt.show()

tdf_ns = df_ns.T
print(tdf_ns)
tdf_ns.plot(kind='barh')
plt.show()

해결1] df_ns = iloc[시작행:끝행,시작열:끝열] 0행~ 5행 ,3열부터 :
df_ns.index = ['South','North']
ㄴdf_ns.columns = df_ns.columns.map(int)



'''