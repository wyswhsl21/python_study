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
import platform
print('현재 컴퓨터 os플랫폼 확인',platform.system())
#-----------------------------------------------------------------------------------------------------
data = [30,15,45,10]
labels = ['포도','사과','딸기','수박']
print(data)
plt.pie(data,labels=labels,autopct='%2.1f%%',startangle=90,textprops=dict(color="w")),
# plt.hist(data,bins=20,color='hotpink',edgecolor='black') # hist 는 그래프 모양 
plt.xlabel('value')
plt.ylabel('data')
plt.show()

print('그래프 차트 ')


'''
해결1] 큰제목, x제목, y제목
해결2] 서브플롯  plt.plot(x,y) 라인차트 
plot(), subplot(), scatter(), savefig()
startangle 은 파이의 시작 차트를 몇도로 할지 결정하는거 90도면 90도에서 시작됨.
'''































print()
print()