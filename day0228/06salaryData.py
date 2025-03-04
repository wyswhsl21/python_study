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
#----------------------------------------------------------------------------------------------
# IQR (Interquartile Range), threshold 임계치 & z_score 개념 원래수치 - 평균값/분산 
path ='./data/salaryData.csv'

df= pd.read_csv(path,encoding='cp949')

# print(df.info())
# #해결 3] null 값 찾는것
# print(df.isna().sum()) #null 값 찾는것

# print(df.describe())

#문제 3] null값 대체
# df.fillna(df['Age'].mean(),inplace=True)
# print(df)
# df.fillna(df['Salary'].mean(),inplace=True)
# print(df)

#해결4 ] 데이터분리 훈련/ 테스트 아니고 x독립변수 Country/Salary , y종속변수 
#Purchased 모든행 국가/급여 독립변수 X권장 , 종족변수
X= df.loc[:,'Country':'Salary']
y= df['Purchased']
# print(y)

#해결 5] LabelEncoder 대상 필드를 Country 국가이름 0 1 2
from sklearn.preprocessing import LabelEncoder
print('*'* 30)
encoder = LabelEncoder() #fit(), fit_transform
X['Country'] = encoder.fit_transform(X['Country'])
print(X)

#해결 5 연장 Y]
encoder_purchased = LabelEncoder()
y = encoder_purchased.fit_transform(y)
print('종족변수 구매 여부', y)
print(X,y)
print()
#해결 5] 크기 조정 MinMaxScaler(), StandardScaler()
from sklearn.preprocessing import StandardScaler,MinMaxScaler

#해결 6] StandardScaler() 처리
SS_X = StandardScaler() # 표준화
SS_X.fit_transform(X)
print(SS_X.fit_transform(X)) #열지도 상관계수
print()
#해결 6] MinMaxScaler() 처리
min_X = MinMaxScaler() #최소치 최대치 정규화
min_sX  = min_X.fit_transform(X)
print(min_sX) 

#해결 7] 훈련 데이터 & test 데이터 분리 8:2 , 7:3 7:2:1
print('\ntrain_test_split 훈련 테스트 데이터 분리')
from sklearn.model_selection import train_test_split
# 1,2,3,4 = train_test_split(X,y,test_size=0.2)
X_train,X_test,y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=3
)
print(X_train)
print()
print(X_test) #2건 훈련 데이터
print()
#정답지 역할 y
print('정답지 역할 y 종속변수')
print(y_train)
print()
print(y_test) #2건 정답지 데이터
print()






'''
'''