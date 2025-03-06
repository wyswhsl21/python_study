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
train= pd.read_csv(path,encoding='cp949')
test= pd.read_csv(test_path,encoding='cp949')




def fill_cabin(pclass, cabin, most_common_cabin):
    if pd.isna(cabin) or cabin == 'Unknown':
        return most_common_cabin[pclass]  # Pclass별 가장 많은 Cabin 할당
    return cabin
#결측값 없애기
test_train_data = [train,test]
print(test_train_data) # PassengerId  Pclass Name Sex Age SibSp Parch Ticket Fare Cabin Embarked
# Age 결측값 채우기
for dt in test_train_data:
    dt['Age'] = dt.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.median())) #Pclass 별로 나이의 평균값 채우기

for dt in test_train_data:
    dt['Embarked'].fillna(dt['Embarked'].mode()[0],inplace=True) # Embarked 최빈값으로 결측값 채우기

for dt in test_train_data:
    dt['Fare'] = dt.groupby('Ticket')['Fare'].transform(lambda x:x.fillna(x.mean())) #티켓 그룹화 화여 요금의 평균으로 결측 채우기
    
for dt in test_train_data:
    dt['Fare'] = dt.groupby(['Pclass', 'Embarked'])['Fare'].transform(lambda x: x.fillna(x.mean()))



#Cabin 결측값 채우기 
for dt in test_train_data:
    dt['Cabin_First_Letter'] = dt['Cabin'].astype(str).str[0]
    most_common_cabin = dt.groupby('Pclass')['Cabin_First_Letter'].apply(lambda x:x.mode()[0])
    dt['Cabin'] =dt.apply(lambda x: fill_cabin(x['Pclass'],x['Cabin'],most_common_cabin),axis=1)



print(train.isnull().sum())
print(test.isnull().sum())
print(train.info())
print(test.info())
print(test[test['Fare'].isnull()])
print(train['Cabin_First_Letter'][:])
print()
print()
