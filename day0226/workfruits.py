import matplotlib
import matplotlib.pyplot as plt        # 첫번째
from  matplotlib import pyplot as plt  # 두번째
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc
import seaborn as sns
import matplotlib.patches as mpatches
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
fruits = ['orange', 'blue', 'gold', 'kiwi'] #index
area = ['서울', '안양', '수원', '일산'] #key
su1 = [21, 34, 45, 13]
su2 = [45, 19, 31, 50]
su3 = [33, 56, 27, 41]
su4 = [77, 26, 65, 29]

#해결 2] 판다스 DataFrame화 df = pd.DataFrame()
# ㄴ 지역별 area kye 값, va
df = pd.DataFrame({area[0]:su1, area[1]:su2,area[2]:su3,area[3]:su4},index=fruits)
print(df)
print()

#해결 3] df대상으로 bar 타입 그래프 생성
# df.plot(kind='bar',figsize=(10,5))




#해결 4] 데이터 값 표시 plt.text()
fruits = ['orange', 'blue', 'gold', 'kiwi']  # 인덱스
area = ['서울', '안양', '수원', '일산']  # 키(컬럼명)
su1 = [21, 34, 45, 13]
su2 = [45, 19, 31, 50]
su3 = [33, 56, 27, 41]
su4 = [77, 26, 65, 29]

ax = df.plot(kind='bar', figsize=(10,7))
for k in range(len(ax.patches)):
    rect = ax.patches[k]
    print(k, '번째  ', rect)
    plt.text(rect.xy[0], rect.get_height(), str(rect.get_height()), fontsize=12)
plt.show() 
time.sleep(1)
#--------------------------------------------------------------------------------------
dft = df.T
ax = dft.plot(kind='bar', figsize=(10,7))
for k in range(len(ax.patches)):
    rect = ax.patches[k]
    print(k, '번째  ', rect)
    plt.text(rect.xy[0], rect.get_height(), str(rect.get_height()), fontsize=12)
plt.show()

'''
# area = ['서울', '안양', '수원', '일산']
# su1 = [21, 34, 45, 13]
# su2 = [45, 19, 31, 50]
# su3 = [33, 56, 27, 41]
# su4 = [77, 26, 65, 29]



'''
'''
ax = df.plot(kind='bar',figsize = (10,7))
for k in range(len(ax.patched)):
    rect=ax.patches[k]
    print(rect)
    plt.text(rect.xy[0],rect.get_height(),rect.get_height())


    




# 막대 그래프 그리기
fig,ax = plt.subplots(figsize=(10, 7))
bar_width = 0.2  # 막대 너비
x = np.arange(len(fruits))  # x 좌표 설정
print(x , 'x의 좌표값')

# 각 지역별로 막대 추가
for i, area_name in enumerate(area):
    bars = ax.bar(x + i * bar_width, df.iloc[i], width=bar_width, label=area_name)

    # 각 막대 위에 숫자 표시 (plt.text 활용)
    for bar in bars:
        height = bar.get_height() #막대의 높이(값).
        ax.text(bar.get_x() + bar.get_width()/2, height, str(height),  #막대 중앙에 숫자 위치.
                ha='center', va='bottom', fontsize=10)

# 축 및 범례 설정
ax.set_xticks(x + bar_width * (len(area) / 2 - 0.5))
ax.set_xticklabels(fruits)
ax.set_xlabel("과일")
ax.set_ylabel("수량")
ax.set_title("지역별 과일")
ax.legend(title="지역")
'''