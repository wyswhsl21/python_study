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
# OpenCV = Open Source Computer Vision 라이브러리 
# pip install opencv-python 설치

#아이리스 붓꽃 iris 3종류 세토사 , 버시킬러, 버지니카
#sepal :꽃받침 , petal: 꽃잎
# iris = sns.load_dataset('iris')
# print(iris)
# print()
# print(iris.info())
# # 

# plt.show()
# print('sns 사본의 이용한 데이터 set')
# sepal_length  sepal_width  petal_length  petal_width  species

#데이터셋 dataset sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


'''
해결1] 훈련,테스트 분리 8:2
해결2] 훈련, 테스트 갯수 종별 갯수
해결3] 모델의 학습 LogisticRegression(), fit() , 예측predict(X_test) 평가 accuracy_score()
해결4] 모델학습과정을 사용자 정의 함수로 만듬

'''
# 데이터 로드
iris = load_iris() #첫번째 에러
print(iris)
print()

#3월5일 수요일 iris 데이터셋 이해, 

X=iris.data # 입력데이터 (특정 값들)
y= iris.target # 타겟 데이터 (클래스)
print('- ' * 35)
print(X)
print(y)

feature_names = iris.feature_names
target_names = iris.target_names
print('- ' * 35)


#해결 1], 해결 2]
'''
X_train: 훈련용 입력 데이터 (80%)
X_test: 테스트용 입력 데이터 (20%)
y_train: 훈련용 정답(타겟) 데이터 (80%)
y_test: 테스트용 정답(타겟) 데이터 (20%)
'''
X_train,X_test,y_train, y_test = train_test_split(iris.data,iris.target,test_size=0.2)
print('X_train 훈련데이터')
print(len(X_train))
print()
print('X_test 테스트 데이터')
print(len(X_test))
print()


print(pd.Series(y_train).value_counts)
print(pd.Series(y_test).value_counts)

#해결 3] 모델의 학습 LogisticRegression(), fit() , 예측predict(X_test) 평가 accuracy_score()
'''
LogisticRegression() → 로지스틱 회귀 모델 생성
fit(X_train, y_train) → 훈련 데이터로 모델 학습
predict(X_test) → 테스트 데이터에 대해 예측 수행
score(X_test, y_test) → 모델의 정확도 평가
'''
lr = LogisticRegression()
lr.fit(X_train,y_train)
y_pred= lr.predict(X_test) #X_test 에 대한 예측값 -> y_pred 
print('예측결과',y_pred)
print('실제정답',y_test)

#정확도 평가
accuracy = accuracy_score(y_test,y_pred)
print(accuracy)

lr_ac = lr.score(X_test,y_test)
print(f'모델 정확도: {lr_ac:.2f}')

dt =DecisionTreeClassifier()