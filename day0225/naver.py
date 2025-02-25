# import matplotlib
# import matplotlib.pyplot as plt        # 첫번째
# from  matplotlib import pyplot as plt  # 두번째
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
url = 'https://finance.naver.com/sise/lastsearch2.nhn'
dfs = pd.read_html(url, encoding='euc-kr')
# print(dfs)
print()

print(len(dfs))
print('-' * 70)

print(dfs[1])
result = dfs[1].dropna() #nan 제거 함수
print(result)
print()

#해결 ] 종목명, 현재가 열추출

df = pd.DataFrame(result,columns=['종목명','현재가'])
pd.set_option("display.unicode.east_asian_width",True)
print(df)
x=df['종목명']
y = df['현재가']

plt.scatter(x,y)
plt.plot(x,y)
plt.tight_layout()
plt.xticks(rotation=45, ha='right')

df.to_csv('./data/naverstack.csv',encoding='cp949',mode='w',index=True)
print('./data/naverstack.csv 저장 성공하였습니다.')
time.sleep(1)
print()
print()
print()
print()
print()
df= pd.read_csv('./data/naverstack.csv',index_col='종목명',encoding='cp949')
# print('*' * 45)
# print(df)
# print('*' * 45)
df.drop(['Unnamed: 0'],axis=1,inplace=True) #inplace 는 객체를 그대로 사용할지 복사본을 만들지에 대한 옵션이다.
ax=df.plot(kind='bar',title='네이버주식')  #문제점 idnex 표시값이 x 축으로 표시됨.

df['현재가'].plot(ax=ax,label='현재가')

plt.show()
#시각화  bar,scatter,plot,pie,hist 비권장
#해결 ] to_csv ('/data/naverstack.csv)


'''
fig, ax1 = plt.subplots(figsize=(12, 6))  #
# Bar Chart (Primary Y-axis)
ax1.bar(df['종목명'], df['현재가'], color='skyblue', label='현재가')
ax1.set_xlabel("종목명")
ax1.set_ylabel("현재가 (원)", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
# Rotate X-axis labels 
ax1.set_xticklabels(df['종목명'], rotation=90)
# Create secondary Y-axis (twin axis) (line chart)
ax2 = ax1.twinx()
ax2.plot(df['종목명'], df['현재가'], color='red', marker='o', linestyle='-', linewidth=2, label='가격 변동')
ax2.set_ylabel("현재가 (라인 차트)", color='red')
ax2.tick_params(axis='y', labelcolor='red')
# Titles 
plt.title("네이버 금융 인기 종목 (Bar + Line Chart)")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()


'''