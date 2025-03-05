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
from sklearn.metrics import accuracy_score ,confusion_matrix
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

fig, axes = plt.subplots(2, 2, figsize=(8, 8))  # 2x2 서브플롯

# (1) 훈련 데이터 클래스 분포
sns.histplot(y_train, bins=3, kde=False, ax=axes[0, 0])
axes[0, 0].set_title('훈련 데이터 클래스 분포')
axes[0, 0].set_xlabel('클래스')
axes[0, 0].set_ylabel('개수')
# (2) 훈련 데이터 산점도
sns.scatterplot(x=X_train[:, 0], y=X_train[:, 1], hue=y_train, palette='deep', ax=axes[0, 1])
axes[0, 1].set_title('훈련 데이터 (산점도)')
axes[0, 1].set_xlabel(iris.feature_names[0])
axes[0, 1].set_ylabel(iris.feature_names[1])
axes[0, 1].legend(title="클래스")
# (3) 혼동 행렬
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, cmap='Blues', fmt='d', xticklabels=iris.target_names, yticklabels=iris.target_names, ax=axes[1, 0])
axes[1, 0].set_title("혼동 행렬 (Confusion Matrix)")
axes[1, 0].set_xlabel("예측값")
axes[1, 0].set_ylabel("실제값")
# (4) 정확도 막대 그래프
accuracy = accuracy_score(y_test, y_pred)
sns.barplot(x=["모델 정확도"], y=[accuracy], ax=axes[1, 1])
axes[1, 1].set_ylim(0, 1)
axes[1, 1].set_ylabel("정확도")
axes[1, 1].set_title("로지스틱 회귀 정확도")

plt.tight_layout()
plt.show()
# class MlIris:
#     def __init__(self,iris):
#         self.iris = iris
#         pass
#     def train_split_data(self):
#         X_train,X_test,y_train, y_test = train_test_split(self.iris.data,self.iris.target,test_size=0.2)
#         return X_train,X_test,y_train, y_test
#     def fit_lr(self,X_train,y_train):
#         lr=LogisticRegression()
#         lr.fit(X_train,y_train)
#         return
#     def ml_predict(self,X_test):
#         y_pred = lr.predict(X_test)
#         return y_pred

#     def ml_accuracy(self,y_test,pr):
#         my_ac = accuracy_score(y_test,pr)
#         return my_ac

# if __name__ == '__main__':
#     try:
#         iris = load_iris()
#         lr = MlIris(iris)
#         X_train,X_test,y_train, y_test = lr.train_split_data()
#         lr.fit_lr(X_train,y_train)
#         pr = lr.ml_predict(X_test)
#         ac = lr.ml_accuracy(y_test,pr)
        
#     except Exception as e:
#         print(f'{e}')
    




