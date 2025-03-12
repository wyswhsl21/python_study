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
# sepal:꽃받침 , petal:꽃잎  iris붓꽃 3종류 세토사setosa, 버시컬러versicolor, 버지니카virginica
# iris = sns.load_dataset('iris') 
# print(iris)
# print()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree  import DecisionTreeClassifier #캐글에서 제공되는  학습모델
from sklearn.metrics import accuracy_score 
from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer

iris = load_iris() 
print(iris) #터미날에 출력된 정보를 보고 키값들 정보를 확인할수 있습니다 
print()
print()
 

X = iris.data
y = iris.target
print(X)
print()
print(y)
feature_names = iris.feature_names #맨마지막라인쯤 - Many, many more ... 다음에 있음
target_names = iris.target_names
print(feature_names)  #['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
print()
print(target_names)  #['setosa' 'versicolor' 'virginica']
print('- ' * 30)
print()
# 해결1] 훈련,테스트 데이터분리 8:2  7:3  from sklearn.model_selection import train_test_split
# 해결2] 훈련,테스트 갯수  종별갯수
# 해결3] 모델의 학습 LogisticRegression(), fit(훈련데이터x, 훈련데이터y),  예측predict(X_test),  평가accuracy_score()
# 해결4] 모델학습과정을 사용자정의함수 def lr_score(X_train,X_test,y_train,y_test): 

# 해결1] 훈련,테스트 데이터분리 8:2   from sklearn.model_selection import train_test_split
# 참고 X_train, X_test , y_train, y_test  =  train_test_split( X국가나이급여데이터, y구매여부, test_size=0.2) 
X_train,X_test,y_train,y_test =  train_test_split(  iris.data, iris.target, test_size=0.2 )
print('X_train훈련데이터') 
print(X_train)
print()
print('X_test테스트데이터')
print(X_test)
print()
print()

# 해결2] 훈련,테스트 갯수  종별갯수
print(pd.Series(y_train).value_counts) #120건
print(pd.Series(y_test).value_counts) #30건

# 해결3] 모델의 학습 LogisticRegression(), fit(),  y_pred=예측predict(X_test), 평가accuracy_score()
# 참고 from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(max_iter=150) #반복횟수 max_iter=150
lr.fit(X_train, y_train) # 훈련데이터  lr.fit(X_train컬럼명, y_train품종)
print('LogisticRegression모델학습으로 fit()훈련을 종료')

y_pred = lr.predict(X_test)
print('LogisticRegression모델학습 lr.predict(X_test)학습후 예측')
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)
print('LogisticRegression모델학습  평가 점수 ', accuracy)
print('- '  * 30)
print()

# 참고 from sklearn.tree  import DecisionTreeClassifier #캐글에서 제공되는  학습모델
dt = DecisionTreeClassifier() 
dt.fit(X_train, y_train) # 훈련데이터  dt.fit(X_train컬럼명, y_train품종)
print('DecisionTreeClassifier모델학습으로 fit()훈련을 종료')

y_pred = dt.predict(X_test)
print('DecisionTreeClassifier모델학습 dt.predict(X_test)학습후 예측')
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)
print('DecisionTreeClassifier모델학습  평가 점수 ', accuracy)
print()


# 해결4] 모델학습과정을 사용자정의함수 def lr_model_score():
# 해결4] 권장사용자정의함수 def lr_score():  
print("사용자정의 함수 def lr_score() ")
def lr_score( X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test):
    lr = LogisticRegression(max_iter=150)  
    lr.fit(X_train, y_train) 
    pred=lr.predict(X_test)
    accuracy=accuracy_score(y_test, pred)
    return (accuracy , pred)
retscore, retprd = lr_score()
print(retprd)   #[1 2 2 0 2 1 0 2 0 1 1 2 2 2 0 0 2 2 0 0 1 2 0 2 1 2 1 1 1 2]
print(retscore) 
print()

# 각자5] 시각화 LinearRegress응용
# X = iris.data
# y = iris.target
# print('iris.target 데이터 다시 확인')
# print(y)




















print()
