# import matplotlib.pyplot as plt        # 첫번째
# from  matplotlib import pyplot as plt  # 두번째
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc
from sklearn.preprocessing import StandardScaler
# 음수표기 관리
import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import pandas as pd
import numpy as np
import time

# 사이킷럿(scikit-learn) 라이브러리 임포트 
from sklearn.datasets import make_classification 
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score, roc_curve  #처음적는 함수 
from sklearn.model_selection import train_test_split

import seaborn as sns 
#--------------------------------------------------------------------------------------------------------------------------------------
# 순서1] sns데이터셋의  titanic로  SVC모델, fit(), 예측,  결과보는방법(시각화, report)
# 처리과정  쥬피터노트북 했던것처럼 처리 
# 처리과정 결측치해결, 필요없던컬럼 삭제, 훈련데이터항목/target정답 survived, test테이터항목//target정답 survived

'''
 survived  pclass     sex   age  sibsp  parch     fare embarked   class    who  adult_male deck  embark_town alive  alone
0           0       3    male  22.0      1      0   7.2500        S   Third    man        True  NaN  Southampton    no  False
1           1       1  female  38.0      1      0  71.2833        C   First  woman       False    C    Cherbourg   yes  False
2           1       3  female  26.0      0      0   7.9250        S   Third  woman       False  NaN  Southampton   yes   True
3           1       1  female  35.0      1      0  53.1000        S   First  woman       False    C  Southampton   yes  False
4           0       3    male  35.0      0      0   8.0500        S   Third    man        True  NaN  Southampton    no   True
..        ...     ...     ...   ...    ...    ...      ...      ...     ...    ...         ...  ...          ...   ...    ...
886         0       2    male  27.0      0      0  13.0000        S  Second    man        True  NaN  Southampton    no   True
887         1       1  female  19.0      0      0  30.0000        S   First  woman       False    B  Southampton   yes   True
888         0       3  female   NaN      1      2  23.4500        S   Third  woman       False  NaN  Southampton    no  False
889         1       1    male  26.0      0      0  30.0000        C   First    man        True    C    Cherbourg   yes   True
890         0       3    male  32.0      0      0   7.7500        Q   Third    man        True  NaN   Queenstown    no   True

전처리 요약:
결측치 처리: deck, embark_town 삭제, age는 삭제, embarked는 각자해결
범주형 변수 처리: sex와 embarked를 원-핫 인코딩.
sex는 female과 male로 변환
embarked는 town_S, town_C, town_Q로 변환
데이터 선택 및 분할: 모델에 사용할 변수 선택, 훈련 데이터와 테스트 데이터 분할.
표준화: SVM모델에 맞게 데이터 표준화.
'''

#1.데이터 로드
df = sns.load_dataset('titanic')
print(df) # [891 rows x 15 columns]
print()
print(df.info()) 
print()

#2. 결측값 확인
print('결측값확인')
print(df.isna().sum())


#3. 불필요한 컬럼 제거
df_new = df.drop(['deck','embark_town'],axis=1)
print(df_new)
#4. 결측값 제거 (age,embarked 컬럼에서)
df_new = df_new.dropna(subset=['age','embarked'],how='any',axis=0) #age널 
print('결측값 제거 됏는지 확인\n',df_new.isna().sum())
# 범주형 데이터 변환
df_new = pd.get_dummies(df_new, columns=['embarked', 'sex', 'class', 'who', 'alive'], drop_first=True)
# 4. 데이터 타입 변환 (bool → int, object → category 변환)

# 5. 불필요한 bool 컬럼을 int로 변환
bool_cols = ['adult_male', 'alone']
df_new[bool_cols] = df_new[bool_cols].astype(int)

#5. 결측값 제거 후 데이터 확인
print(df_new) # [714 rows X 13 columns ]
print(df_new.isna().sum()) #결측값 있는지 확인하기
print('- ' * 50)



# X= df_new.iloc[:,1:]
# y= df_new['survived']
X = df_new.drop(columns=['survived'])  # 생존 여부를 제외한 나머지를 입력 변수로 사용
y = df_new['survived']  # 생존 여부 (목표 변수)
#5. 훈련/테스트 데이터 분할 (순서 수정)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print("🔍 X_train 데이터 타입 확인:")
print(X_train.dtypes)

#데이터 정규화
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # 훈련 데이터 정규화
X_test_scaled = scaler.transform(X_test)  # 테스트 데이터 정규화


#모델 학습 svc 사용
md = SVC(kernel='linear',C=1.0,random_state=42)
md.fit(X_train_scaled,y_train)

# 예측
y_pred = md.predict(X_test_scaled)
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#성능 평가
accuracy = accuracy_score(y_test,y_pred) #정확도 계산
conf_matrix = confusion_matrix(y_test,y_pred) #혼동 행렬
class_report = classification_report(y_test,y_pred)

print(f'모델 정확도:{accuracy:4f}\n')
print('분류보고서:' , class_report)


#4. 혼동 행렬 시각화
plt.figure(figsize=(5,4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Survived', 'Survived'], yticklabels=['Not Survived', 'Survived'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()
# 인코딩 방법 첫번째 LabelEncoder 화 두번째 sex_mapping{0:'',1:''} 컬럼.map(sex_mapping)
# 3번째 pd.get_dummies()
# 순서1] 
# 순서1] 
# 순서1] 
# 순서1] 
# 순서1] 
# 순서1] 


'''
데이터 준비 (데이터프레임 생성)
데이터 전처리 (결측값 처리, 정규화, 훈련/테스트 분할)
모델 선택 및 학습 (Scikit-learn 활용)
모델 평가 (성능 지표 확인)
결과 시각화 (Confusion Matrix, ROC Curve 등)
'''










print()
print()