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
#-------------------------------------------------------------------------------------------
path = './data/salaryData.csv'

# 해결1] 판다스 read_csv
# 해결2] info() 문제점 
# 해결3] 열컬럼별 널갯수 확인 

df = pd.read_csv(path)
print(df)
print()

print(df.info())
print()

print(df.isna().sum())
print()

# 문제 3]  null값 대체
# ㄴ열컬럼널  확인 Age컬럼   null값 대체
# ㄴ열컬럼널  확인 Salary컬럼 null값 대체

# 권장 df['Age'] = df['Age'].fillna(df["Age"].mean()).astype(int)
# 편리 df = df.fillna( df.mean(numeric_only=True)) 

for col in df.columns:
    most_frequent = df[col].mode()[0]
    df[col].fillna(most_frequent, inplace=True)

# print("\n결측치 처리 후:")
# print(df.isna().sum())
print(df)
print()

# print(df.info()) #필드 속성 타입 
# print()

# print(df.describe(include='all'))  #숫자타입에 대한 숫자함수 적용
# print()


# 해결4]  x독립변수 Country~Salary  , y종속변수 Purchased
#   모든행  국가/급여  독립변수 X권장 , 종족변수 
X = df.loc[ :  , 'Country':'Salary']
y = df['Purchased']
# print(X)
# print(y)

# 해결5] LabelEncoder 대상필드를 Country 국가이름 0 1 2 
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder() # fit(), fit_transform
X['Country'] = encoder.fit_transform(X['Country'])
print(X)

# 해결5연장 y구매여부도 0 1 표시 
encoder_y = LabelEncoder() # fit(), fit_transform
y= encoder_y.fit_transform(y)
print('종족변수 구매여부 ', y)
print()

# 해결6] 크기 조정 StandardScaler(), MinMaxScaler()
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 해결6중에서 StandardScaler 처리
ss_x = StandardScaler()
ss_x2 = ss_x.fit_transform(X)
print(ss_x2)
print()


# 해결6중에서 StandardScaler MinMaxScaler 최소 0 최대 1
mm_x = MinMaxScaler()
mm_x2 = mm_x.fit_transform(X) 
print(mm_x2)
print()

# 해결7] 훈련데이터  & test데이터 분리 8:2  7:3   
print('\ntrain_test_split 훈련 테스트 데이터 분리')
from sklearn.model_selection import train_test_split
X_train, X_test , y_train, y_test  =  train_test_split( X, y, test_size=0.2) #, random_state=3 시드값역할
print(X_train)
print()
print(X_test)  #2건  test데이터
print()

#정답지역할 y
print('정답지역할 y 종속변수 ')
print(y_train)
print()
print(y_test) #2건 정답지데이터
print()
'''
   Country   Age   Salary Purchased
0   France  44.0  72000.0        No
1    Spain  27.0  48000.0       Yes
2  Germany  30.0  54000.0        No
3    Spain  38.0  61000.0        No
4  Germany  40.0  48000.0       Yes
5   France  35.0  58000.0       Yes
6    Spain  27.0  52000.0        No
7   France  48.0  79000.0       Yes
8  Germany  50.0  83000.0        No
9   France  37.0  67000.0       Yes

'''












































print()
print()
