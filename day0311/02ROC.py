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

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import auc, confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
#--------------------------------------------------------------------------------------------
# 해결1 Social_Network_Ads.csv파일 읽기 , 정보확인info, 컬럼, 널값, 구조 등등 확인
# 해결2 from sklearn.model_selection import train_test_split(훈련데이터, 정답지, 분리테스트2/훈련8)
  #ㄴ보충 train_data대신 X,  target대신y
# 해결3 train_data대신 X훈련데이터  MinMaxScaler적용 
# 해결4 train_test_split() 데이터분리 훈련,테스트 분리 
# 해결5 학습모델선택, fit(), predict()결과는 [0 0 0 1 0 1 0 0 0  ~ ~  0 1 0 1 1 0 0 0  1 0 0 1 1 0]  

# from sklearn.metrics import confusion_matrix 
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import classification_report
  #ㄴ 해결6  confusion_matrix
  #ㄴ 해결6  accuracy_score
  #ㄴ 해결6  classification_report구매/비구매 전체데이터중 구매% 비구매%  시각화표현 [0 0 0 1 0 1 0 0 0  ~ ~  0 1 0 1 1 0 0 0  1 0 0 1 1 0]


'''
classification_report 반드시 ROC 커브 = Receiver Operating Characteristic " 커브로 binary classfication 모델 
ROC 커브 = Receiver Operating Characteristic 커브로 binary classification 모델 
ROC커브 = Receiver Operating Characteristic" 커브로 binary classification 모델
AUC는 "Area Under  Curve "  ROC 커브 아래 부분의 면적의 너비를 말합니다.

              precision    recall    f1-score   support

           0       0.79      0.90      0.84        58
           1       0.82      0.67      0.74        42

    accuracy                           0.80       100
   macro avg       0.81      0.78      0.79       100
weighted avg       0.80      0.80      0.80       100
'''

print('- ' * 50)


from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score,roc_curve #처음적는 함수
from sklearn.model_selection import train_test_split
# ------------------------------------------------------------------------------------------------ 처음 적는 함수

# DecisionTreeClassifier, LogisticRegression, SVC 성능 비교해서 ROC 커브 그래프 표시
# 순서 1] 데이터 발생
X,y = make_classification(n_samples=10000, n_classes=2,)
print('X데이터')
print(X)
print()
time.sleep(1)
print('y데이터')
print(y)
print()

#순서 2] 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

#순서 3] 모델 생성 dt,lr svc / fit(훈련x, 훈련y)
dt = DecisionTreeClassifier()
lr = LogisticRegression()
svc = SVC(probability=True)

dt.fit(X_train,y_train)
lr.fit(X_train,y_train)
svc.fit(X_train,y_train)

y_pre_dt = dt.predict_proba(X_test)[:,1]
y_pre_lr = lr.predict_proba(X_test)[:,1]
y_pre_svc = svc.predict_proba(X_test)[:,1]


#순서 4] score, accuracy 데이터 생성, 데이터 훈련 테스트 분리, 모델 생성 / 모델 fit()/ predict(x_test)
#from sklearn.metrics import roc_auc_score, roc_curve #처음 적는 함수

fpr_dtc,tpr_dt,_ = roc_curve(y_test,y_pre_dt)
fpr_lr , tpr_lr,_ = roc_curve(y_test,y_pre_lr)
fpr_svc , tpr_svc,_ = roc_curve(y_test,y_pre_svc)

roc_auc_dt_score = roc_auc_score(y_test,y_pre_dt)
roc_auc_lr_score = roc_auc_score(y_test,y_pre_lr)
roc_auc_svc_score = roc_auc_score(y_test,y_pre_svc) #AUC 계산



'''
auc(fpr, tpr): FPR과 TPR을 사용해 AUC 계산
roc_auc_score(y_test, y_score): 실제 정답(y_test)과 예측 점수(y_score)로 AUC 계산
'''


plt.plot(fpr_dtc,tpr_dt, color='red',label=f"ROC curve (AUC={roc_auc_dt_score:.2f})")
plt.plot(fpr_lr , tpr_lr, color='green',label=f"ROC lr curve (AUC ={roc_auc_lr_score:.2f})")
plt.plot(fpr_svc , tpr_svc, color='blue',label=f"ROC svc curve (AUC ={roc_auc_svc_score:.2f})")
plt.plot([0,1],[0,1],'k--')



plt.title('ROC커브 그래프')
plt.xlabel('')
plt.ylabel('')
plt.legend()
plt.show()
'''
# ROC커브 = Receiver Operating Characteristic" 커브로 binary classification 모델의 퍼포먼스를 나타내는 그래프입니다
#그래프의 X축은 False Positive Rate(FPR) Y축은 True Positive Rate(TPR)을 나타냅니다.
# AUC는 "Area Under  Curve "  ROC 커브 아래 부분의 면적의 너비를 말합니다.
Sensitivity:  tpr=TPR(True Positive Rate)는  Positive로 예측된 것들 중 진짜 Positive인 것의 비율을 나타냅니다. ( TPR = TP / (TP+FN) )
Specificity : tnr=TNR(True Negative Rate)는  Negative로 예측된 것들 중 진짜 Negative인 것의 비율을 나타냅니다. (TNF = TN / (TN + FP))                           

'''
import os
#순서 1]
if not os.path.exists('gif_frames'):
    os.makedirs('gif_frames')
    print('gif_frames 폴더 생성 성공했습니다.')

#순서 2] nba_source.csv

#순서 3]

#순서 4]

#순서 5]

#순서 6]

print()
print()
