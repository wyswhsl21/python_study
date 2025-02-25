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

'''
해결1] df_ns = iloc[시작행:끝행,시작열:끝열] 0행~ 5행 ,3열부터 :
df_ns.index = ['South','North']
ㄴdf_ns.columns = df_ns.columns.map(int)



'''