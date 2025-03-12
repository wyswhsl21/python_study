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

train = pd.read_csv('./titanic/train.csv')
test = pd.read_csv('./titanic/test.csv')
print(train)#train 0~890맨끝번호   PassengerId  Survived(생사)  Pclass   Name   Sex   Age  SibSp  Parch   Ticket  Fare Cabin Embarked
print()
print(test)#test   0~417맨끝번호   PassengerId                  Pclass   Name   Sex   Age  SibSp  Parch  Ticket  Fare Cabin Embarked
print()
print()

print(train.info()) #데이터 셋 확인하기
print()
print(test.info())
print()

print(train.columns) #컬럼 보기
print()
print(test.columns)
print()

print(train.dtypes) #type 보기
print()

print(test.dtypes)
print()

print(train.shape,' ') #row x colums 보기 
print()
print(test.shape,' ')
print()

#그래프 사용자 함수
def bar_chart(feature):
    survived = train[train['Survived'] == 1][feature].value_counts()
    dead = train[train['Survived'] == 0][feature].value_counts()
    df = pd.DataFrame([survived,dead])
    df.index = ['survived','dead']
    df.plot(kind='bar',figsize=(10,7))
    plt.show()


# bar_chart('Sex')
print(' ', train['Pclass'].unique())
print(' ', train['Pclass'].value_counts())
# bar_chart('Pclass')

train_test_data = [train, test]

for dt in train_test_data:
    dt['Title'] = dt['Name'] #정규식추천, 정규식 대신 str.extract() .을 기준으로 

for dt in train_test_data:
    dt['Title'] = dt['Name'].str.extract(r'([a-zA-Z]+)\.')
print('- '* 40)
print(train)
print('3교시 11시 12분')
print('train의 Title',train['Title'].value_counts())
print()
print('test의 Title' ,test['Title'].value_counts())
print('- ' * 50)

print()
# print('train_test_data타입 ', type(train_test_data)) #train_test_data타입  <class 'list'>


# 해결]  Embarked: 탑승 항구, C = Cherbourg, Q = Queenstown, S = Southampton

















print()
print()
