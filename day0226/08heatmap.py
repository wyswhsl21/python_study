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

import seaborn as sns




df = pd.DataFrame({'소득':[57327, 93767, 39410, 94951, 59090, 34628, 31809, 46232, 78707, 37816, 47085, 58394, 77072, 97746, 50302, 61129, 83154, 42798, 93530, 84912],
                   '교육':[10, 9, 8, 15, 15, 11, 13, 15, 16, 9, 8, 9, 13, 15, 14, 16, 16, 13, 9, 9],
                   '태도':[9, 5, 10, 6, 10, 9, 7, 7, 5, 7, 8, 9, 6, 1, 5, 5, 7, 2, 4, 4],
                   '투표':[3, 5, 3, 5, 3, 3, 1, 4, 4, 1, 1, 5, 5, 5, 5, 3, 4, 3, 4, 2]})


print(df)

print('- ' *45)
corr = df.corr()
print(corr) #소득        교육        태도        투표

# for i in range(len(corr)):
#     for j in range(i, len(corr)): 
#         corr.iloc[i, j] = np.nan  



mask = np.zeros_like(corr,)
print(mask,'mask')
mask[np.triu_indices_from(mask)] =1
print(mask)
print('*'*30)
new_mask =corr.iloc[1:,:-1]
print(new_mask)
new_mask1 = mask[1:,:-1]
new_mask2 = corr.iloc[1:,:-1]
print('*'*45)
print(new_mask1)
print('*'*45)
print(new_mask2)

print('*'*30)
# mask = np.triu(np.ones_like(corr,dtype=bool)) # triu는 아래 마스크 , tril은 위에것만 남겨놓는것
print(mask)
sns.heatmap(corr,annot=True,cmap='coolwarm',fmt='.2f',linewidths=0.5,mask=mask)
plt.title('나라별 소득 교육 태도 투표')
plt.show()


#해결 1] 판다스 상관계수 corr() 
#해결 2] 피어슨 , 무조건 heatmap () 열지도
#해결 3] heat map  대각을 기준으로 1 1 1
#해결 4] 그룹화 해서 차트 bar,line,pie 