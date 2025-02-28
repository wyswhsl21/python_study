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
import time

#-----------------------------------------------------------------------------------------------------
path ='./data/남북한발전전력량.xlsx'
df = pd.read_excel(path ,engine='openpyxl')
# print(df)  #[9 rows x 29 columns]
# print()

# 해결1] north의 5:8까지의 모든데이터 가져오기 loc[5:8] 
df = df.loc[5:8]
print(df)
print()

# 해결2] 전력량 (억㎾h) 열컬럼 삭제 drop
df.drop('전력량 (억㎾h)', axis='columns', inplace=True)
print(df)
print()

# 해결3] "발전 전력별" 필드 숫자 index 대체 
df.set_index('발전 전력별', inplace=True)
print(df)
print()


# 해결4] 년도를 행으로  합계, 수력, 화력을 열컬럼 대체 
df = df.T
print(df)
print()

ax1 = df[['수력','화력']].plot(kind='bar', figsize=(16, 8), width=0.7, stacked=True)   #, stacked=True
plt.title('북한 전력 발전량 (1990 ~ 2016)', size=20)
ax1.legend(loc='upper right')
ax1.set_xlabel('year년도')
ax1.set_ylabel('발전량(KWh)')
ax1.set_ylim(0, 300)
# plt.show()  기술하면 에러발생합니다 

# 해결5] shift(1) : 합계 한 칸 아래로 이동 
df['합계-1년'] = df['합계'].shift(1)
print(df)
print('- ' * 30)
print()

df['증감율'] = ((df['합계']/ df['합계-1년'])-1) * 100 
print(df)
print()

ax2 = ax1.twinx()
ax2.plot(df.index, df['증감율'] , ls='--' , marker='o', markersize=25, color='green' ) 
ax2.set_ylabel('전년 대비 증감율 추이(%)') # y축 레이블
ax2.set_ylim(-50, 50) # y축 limit
plt.show()





'''
처음실습한 예제
df_ns = df.iloc[ [0,5] , 2:]
print(df_ns)  #[9 rows x 29 columns]
print()
df_ns.index = ['South', 'North']  

df_ns = df.iloc[ [0,5] , 2:]
print(df_ns)  #[9 rows x 29 columns]
print()
df_ns.index = ['South', 'North']  
# df_ns.columns = df_ns.columns.map(int)  엑셀에서  '1997
# print(df_ns.columns)
print()

# df_ns.plot() 비권장 한쪽집중 가독성이 떨어짐
# plt.show()
tdf_ns = df_ns.T
print(tdf_ns) 

tdf_ns.plot()
plt.show()

# tdf_ns.plot(kind='bar')  추천 
plt.show()

tdf_ns.plot(kind='area')
plt.show()

tdf_ns.plot(kind='barh')
plt.show()

'''




















print()
print()