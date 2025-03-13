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
import imageio
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import auc, confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
#--------------------------------------------------------------------------------------------
print('- ' * 50)
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score,roc_curve #처음적는 함수
from sklearn.preprocessing import MinMaxScaler

# ------------------------------------------------------------------------------------------------ 처음 적는 함수
#iris, 타이타닉, salaryData 종속변수 target 대상 데이터를 전부 숫자 0/1 대신 문자대체
#시각화 다양하게 해서 plt.show() 처리안하면 폴더에 저장후 ~~ .gif 확장로 동영상처럼 play

import os
df= pd.read_csv('./test/nba_source.csv')
print(df)
print()


#순서 1 drop 으로 Award 결측값 삭제
df.drop(columns=['Awards'], inplace=True)


#순서 2 모든 필드값을 평균값으로 null 결측값 대체
for dt in df :
   df[['3P','3P%', 'FG','2P%','FT%','TRB','BLK']] =df[['3P','3P%', 'FG','2P%','FT%','TRB','BLK']].apply(lambda col: col.fillna(col.mean()))

test_df = df.iloc[:100]

# 승패 예측 해보기

#데이터 분할(80%, 20%) 
train,test = train_test_split(test_df, test_size=0.2,random_state=42)
print(train,'train')
print('- ' * 50)
print()
print(test)
print('test')
#훈련 데이터x , 훈련라벨y
#test 데이터x , test라벨y
print()
print(df.info())
print('- ' * 30)


# 결측값 갯수
#해결 결측값은 100% 숫자라서 평균값으로 대체 , Awards 필드 삭제
#해결 [500 rows x 32 columns] 대신 [100 rows x 31 columns] 추출
#해결 훈련,테스트 데이터 분리 8/2 random_state =42 
#정답지 target 선정
#SVC 모델 생성 (c,gamma) 사용
#fit(),predict(),accuracy_score 평가
