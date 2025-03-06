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
#--------------------------------------------------------------------------------------------
#해결 1] titanic 폴더 열기 
path = './titanic/train.csv'
test_path = './titanic/test.csv'
df_train= pd.read_csv(path,encoding='cp949')
df_test= pd.read_csv(test_path,encoding='cp949')
print(df_train)
print()
print(df_test)


print()
# print('train is null()갯수',df_train.isnull().sum())
# print('test is null()갯수',df_test.isnull().sum())
#해결 2] 결측값 확인

#test 총 데이터 418건 훈련 총 데이터 891건
#해결 3] train_test_data =[train,test]
train_test_data = [df_train,df_test]




#해결 5] Age 필드 결측값이 평균 중앙 각자 해결

from sklearn.impute  import SimpleImputer
si = SimpleImputer(strategy='median')
si.fit(df_train[['Age']])
df_train['Age'] = si.transform(df_train[['Age']]).round(2)
df_test['Age'] = si.transform(df_test[['Age']]).round(2)

 
for dt in train_test_data:
    dt['Embarked'].fillna('S', inplace=True)




#해결 4] Name 필드값 조정 Nick 필드,  Title 필드 대체

#해결 5] Embarked : 탑승 항구 , C= Cher

#해결 6] Cabin A B ~~ FGT
cabin_mapping = {'A':0,'B':1,'C':1,'D':1,'E':1,'F':1,'G':1,'T':3,}
for dt in train_test_data:
    dt['Cabin'] = dt['Cabin'].astype(str)[0]
    dt['Cabin'] = dt['Cabin'].map(cabin_mapping)
    dt['Cabin'] = dt.groupby('Pclass')['Cabin'].transform(lambda x: x.fillna(x.mean()))
    dt['Cabin'].fillna(0,inplace=True)
    
#결측값

# Embarked: 탑승 항구, C = Cherbourg, Q = Queenstown, S = Southampton



#해결 7] test 데이터 Fare 금액 
for dt in train_test_data:
    dt['Fare'] = dt.groupby('Pclass')['Fare'].transform(lambda x: x.fillna(x.mean()))


print(df_test.info())
print()
print(df_train.info())
print()
print(train_test_data[0].isnull().sum())
print(train_test_data[1].isnull().sum())

print()
print()
