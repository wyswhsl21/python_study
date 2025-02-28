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
url = 'https://finance.naver.com/sise/lastsearch2.nhn'
dfs = pd.read_html(url, encoding='euc-kr')
print(dfs)
print()

# print( len(dfs), '테이블로 구성되어 있습니다')
# print( '- ' * 70)
# print()

# print(dfs[0])
# print()

print(dfs[1])
pd.set_option("display.unicode.east_asian_width",True)
print()
print()

result = dfs[1].dropna() #NaN전부제거result = dfs[1].dropna(how='all') 
print(result)
print('result결과 데이터 확인 ok')

# 해결1] 종목명, 현재가 열추출 

df = pd.DataFrame(result , columns=['종목명', '현재가'])
pd.set_option("display.unicode.east_asian_width",True)
print(df)
print()
print()
# 해결2] to_csv('./data/naverstack.csv')  저장 
df.to_csv('./data/naverstack.csv', encoding='cp949', mode='w', index=True)
# df.to_csv('./data/naverstack.csv', encoding='cp949', mode='w', index=False) #index=False
print('./data/naverstack.csv 저장 성공했습니다 ')
time.sleep(1)

df = pd.read_csv('./data/naverstack.csv',  index_col='종목명',  encoding='cp949')
# print('* ' * 45)
# print(df)
# print('* ' * 45)

df.drop( ['Unnamed: 0'] , axis=1, inplace=True)
df.plot(kind='bar', title='네이버주식') #문제점 index표시값이 x축표시
plt.show()
print('판다스 df 그래프 차트 OK')
# 해결3] 시각화 bar(), scatter(), plot(), pie()비권장, hist()비권장



'''
아래처럼 에러 메세지 나오면 pip install 명령어로 설치 먼저 하세요 
ImportError: Missing optional dependency 'lxml'.  Use pip or conda to install lxml.
~~\day0225>  pip install lxml

ImportError: Missing optional dependency 'html5lib'.  Use pip or conda to install html5lib.
~~\day0225>  pip install  html5lib
'''















print()
print()