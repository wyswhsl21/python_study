import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt        # 첫번째
from  matplotlib import pyplot as plt  # 두번째
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

#음수표기 관리 

# 음수표기 관리
import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)




data_dict = { 
    'Name': ['aaa', 'bbb',  'ccc',  'ddd',  'eee',  'fff' , 'eee','kim','lee'] ,
    'City': ['수원', '뉴욕', '수원', '서울', '수원', '인천', '뉴욕','인천','서울'] ,
    'Years': [2001,  2023,   1995,  1990,   1985,   2023,   2001,1995,1997 ]
}

df = pd.DataFrame(data_dict)
print(df)
print('- ' *45)
df_group = df.groupby('City') #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001DDDD13F500>
print(df_group)
print('- ' *45)

for key,gg in df_group:
    print(key , ' ', gg)
    print()
print('- ' *45)

# df_group_mean = df_group.mean()
# print(df)

# df_group_year = df.groupby('City')['Years'].mean()
# print(df_group_year)
print('- ' *45)

data = {
        '학년': ['1학년', '1학년', '2학년', '2학년', '3학년', '3학년', '3학년'], 
        '성별': ['남', '여', '남', '여', '남', '여', '여'], 
        'kor': [80, 90, 70, 60, 85, 95, 75] }

df=pd.DataFrame(data)
print(df)
print('- ' *45)


df_group = df.groupby('학년')
df_group_kor = df_group['kor'].agg(['mean','min','max','count'])
print(f'{df_group_kor}')
print('- ' *45)

'''
해결2] 그룹을 학년으로 그룹의 kor 국어점수 평균 출력

'''

data = {'국가': ['한국', '한국', '미국', '미국', '일본', '일본', '한국', '미국', '일본'], 
        '성별': ['남', '여', '남', '여', '남', '여', '남', '여', '남'], 
        '키': [170, 160, 180, 170, 165, 155, 175, 185, 175], 
        '몸무게': [70, 60, 80, 65, 70, 50, 75, 85, 70]}

df = pd.DataFrame(data)
df_group_contry = df.groupby('국가')
df_group_tall = df_group_contry['키'].agg(['mean','min','max','count'])
df_group_weight = df_group_contry['몸무게'].agg(['mean','min','max','count'])

df_group_weight.plot(kind='bar')



plt.show()

print('- ' *45)
table = pd.pivot_table(df,index=['국가','성별'], values=['키','몸무게'],aggfunc=np.mean)
print(table)


# 해결3] 그룹화 컬럼대상 정하고, 키,몸무게 평균화