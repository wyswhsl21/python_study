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
print(train) #train 891갯수  Survived컬럼   PassengerId   Pclass   Name   Sex   Age  SibSp  Parch   Ticket  Fare Cabin Embarked
print()
print(test) #test  418갯수                  PassengerId    Pclass   Name   Sex   Age  SibSp  Parch  Ticket  Fare Cabin Embarked
print()
print()

print(train.info())
print()
print(test.info())
print()

print(train.columns)
print()
print(test.columns)
print()

print(train.dtypes)
print()
print(test.dtypes)
print()

print(train.shape, '  ',test.shape, ) #훈련(891행, 12컬럼)    테스트(418행, 11컬럼)
print()
print()

#그래프 함수 사용자정의
def bar_chart(feature):
    survived = train[train['Survived'] == 1][feature].value_counts()
    dead = train[train['Survived'] == 0][feature].value_counts()
    df = pd.DataFrame( [survived,dead])
    df.index = ['survived', 'dead']
    df.plot(kind='bar', figsize=(10,7))
    plt.show()


bar_chart('Sex') #함수호출

print("train['Pclass'].unique() 결과" , train['Pclass'].unique()) # [3 1 2]
print("train['Pclass'].value_counts() 결과" , train['Pclass'].value_counts()) 

bar_chart('Pclass') #함수호출  # Pclass: 티켓의 선실 등급, 1 = 일등석, 2 = 이등석, 3 = 삼등석



print()
print("train['Embarked'].unique() 결과" , train['Embarked'].unique()) # ['S' 'C' 'Q' nan]
print("train['Embarked'].value_counts() 결과" , train['Embarked'].value_counts()) 

bar_chart('Embarked') #


print()
print(train) #train 891갯수  Survived컬럼   PassengerId   Pclass   Name   Sex   Age  SibSp  Parch   Ticket  Fare Cabin Embarked
print()
print(test) #test  418갯수                  PassengerId    Pclass   Name   Sex   Age  SibSp  Parch  Ticket  Fare Cabin Embarked
print()


train_test_data = [train, test]
print('train_test_data타입 ', type(train_test_data)) #train_test_data타입  <class 'list'>

for dt in train_test_data:
    dt['Title'] = dt['Name'].str.extract('([a-zA-Z]+)\.')  #정규식추천, 정규식대신 str.extract( )권장 Mr.  Miss.  Mrs.  Master.

print('- ' * 50)
print('3교시 11시 29분 ')
print('train의 Title ',train['Title'].value_counts())
print()
print('test의 Title ', test['Title'].value_counts())
print()


print(train.info())
print()
print(test.info())
print()

print('점심식사후  바그래프 확인 1:19')

print(train['Sex'].unique()) #array(['male', 'female'], dtype=object)
print()
print(test['Sex'].unique())  #array(['male', 'female'], dtype=object)







print()
print()
