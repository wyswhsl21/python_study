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
fname = './data/sam_kospi.xlsx'
sam = pd.ExcelFile(fname,engine='openpyxl') 
print(sam) #<pandas.io.excel._base.ExcelFile object at 0x000002633657CAA0>
# 해결 2] 모든 행 , 모든 열 출력
kospi = sam.parse('sam_kospi') #엑셀파일을 파싱 해주기.
print(kospi)
print('*' * 30)
#해결3 ] 모든행 최고, 최소 , 거래량
print(kospi[['Low','High','Volume']])

print('*' * 30)
#해결 4] kospi 접근 최고 High컬럼 평균, 최저 Low컬럼 평균
print(kospi.loc[:,['High','Low','Date','Volume']])
print('*' * 30)
print(kospi.iloc[:,[0,2,3,5]])
print('*' * 30)
print((kospi[['High']].mean()))
print('*' * 30)
print((kospi[['Low']].mean()))
'''




'''