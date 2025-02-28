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
df = pd.read_excel(path , engine='openpyxl')
print(df)  #[9 rows x 29 columns]
print()
print()

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

tdf_ns.plot(kind='bar')
plt.show()


tdf_ns.plot(kind='area')
plt.show()

tdf_ns.plot(kind='barh')
plt.show()

# 해결1] df_ns = iloc[ [시작행,끝행] ,  시작열:끝열 ] 0행,5행 , 2열부터:
#   df_ns.index = ['South', 'North'] 
#   df_ns.columns = df_ns.columns.map(int)
#   print(df_ns)







'''
아래처럼 에러 메세지 나오면 pip install 명령어로 설치 먼저 하세요 
ImportError: Missing optional dependency 'lxml'.  Use pip or conda to install lxml.
~~\day0225>  pip install lxml

ImportError: Missing optional dependency 'html5lib'.  Use pip or conda to install html5lib.
~~\day0225>  pip install  html5lib

# ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.
~~\day0225>  pip install  openpyxl
'''















print()
print()