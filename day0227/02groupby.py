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



data_dict = { 
    'Name': ['aaa','bbb','ccc',	'ddd','eee','fff' ,'eee', 'kim'] ,
    'City': ['수원', '뉴욕', '수원', '서울', '수원', '인천', '뉴욕', '인천'] ,
    'Years': [2001,  2023, 1995,1990,1985,2023,	2001, 2024 ]
}


df = pd.DataFrame(data_dict)
print(df)
print('- ' * 30)
print()

# 해결1] City도시별 그룹화
# df_group = df.groupby('City')
# print(df_group ) #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002CB87404920>
# for key , gg  in df_group:
#     print(key, ' ', gg)
#     print()

# df_group_mean = df_group.mean()
# print(df_group_mean)

# df_group_year = df.groupby('City')['Years'].mean()
# print(df_group_year)
# print()

data = {
        '학년': ['1학년', '1학년', '2학년', '2학년', '3학년', '3학년', '3학년'], 
        '성별': ['남', '여', '남', '여', '남', '여', '여'], 
        'kor': [80, 90, 70, 60, 85, 95, 75] }
df = pd.DataFrame(data)
print(df)
print()

# 해결2] 그룹으로  학년하시고 kor국어점수 평균
groupTest = df.groupby('학년')['kor'].mean()
print(groupTest)
print()


# 해결3] 그룹으로  학년하시고 kor국어점수 평균,최소,최대,갯수count agg()
groupTest2 = df.groupby('학년')['kor'].agg(['sum','mean', 'min', 'max', 'count'])
print(groupTest2)
print('- ' * 30)
print()



data = {'국가': ['한국', '한국', '미국', '미국', '일본', '일본', '한국', '미국', '일본'], 
        '성별': ['남', '여', '남', '여', '남', '여', '남', '여', '남'], 
        '키': [170, 160, 180, 170, 165, 155, 175, 185, 175], 
        '점수': [70, 100, 80, 65, 70, 30, 75, 85, 70]}

# 해결4] 각자 그룹화 컬럼대상 정하고 집합함수 사용하고자 하는걸 사용
df = pd.DataFrame(data)
print(df)
print()

groupTest3 = df.groupby('국가')['점수'].sum()
print(groupTest3)
groupTest3.plot(kind='bar')
plt.show()
print()

table = pd.pivot_table(df, index=['국가', '성별'], values=['키','점수'], aggfunc=np.mean)
print(table)



print()
