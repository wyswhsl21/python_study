# import matplotlib
# import matplotlib.pyplot as plt        # 첫번째
# from  matplotlib import pyplot as plt  # 두번째
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

# 음수표기 관리
import matplotlib as mpl
from sklearn.linear_model import LinearRegression
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import pandas as pd
import numpy as np
import seaborn as sns 
import time
#선형 회귀 성능 평가 모델 
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import root_mean_squared_error
#--------------------------------------------------------------------------------------------
# 해결 02 잔차
x =  [13, 19, 16, 14, 15, 14]
y =  [40, 83, 62, 48, 58, 43]

df = pd.DataFrame({'x':x,'y':y})
print('df\n',df)

#선형회귀 시작 fit으로 학습 시키고
lr = LinearRegression()
lr.fit(df[['x']],df['y'])
#예측값 만들기
y_pred = lr.predict(df[['x']])

fig,ax =plt.subplots(2,2, figsize=(10,10))
ax[0,0].plot(df['x'],y_pred,color='green',label='predict')
ax[1,0].scatter(df['x'],df['y'],color='red',label='actual')
ax[0,1].plot(df['x'],y_pred,color='green',)
ax[0,1].scatter(df['x'],df['y'],color='red',)
for i,v in enumerate(df['x']):
    ax[0,1].text(v,df['y'][i],f'({df["x"][i]},{df["y"][i]})')
fig.legend()
plt.show()
#선형 회귀 성능평가하기 실제값과 예측값 넣어주기
mse= mean_squared_error(y,y_pred)
mae = mean_absolute_error(y,y_pred) 
r2 = r2_score(y,y_pred) 
mape = mean_absolute_percentage_error(y,y_pred) 
rmse = root_mean_squared_error(y,y_pred) 
print(f'mse ={ mse}')
print(f'mae ={ mae}')
print(f'r2 ={ r2}')
print(f'mape ={ mape}')
print(f'rmse ={ rmse}')



'''
알고리즘	fit()의 역할
선형 회귀 (LinearRegression)	최적의 w, b 찾기
로지스틱 회귀 (LogisticRegression)	확률적 분류를 위한 가중치 학습
의사결정나무 (DecisionTreeClassifier)	데이터에 최적화된 트리 구조 생성
랜덤 포레스트 (RandomForestClassifier)	여러 개의 결정 트리를 학습
신경망 (MLPClassifier)	가중치와 편향을 최적화
'''


'''
회귀 모델의 성능을 평가할 때 사용되는 주요 지표인 MAE,MSE,RMSE,MAPE,R2_Score 등이 있다.

## 회귀 모델 평가 지표 분석

### 1. MAE (Mean Absolute Error, 평균 절대 오차)
**공식:**

- 실제 값과 예측 값의 차이의 절댓값을 평균낸 값
- 값이 작을수록 모델의 성능이 좋음
- 이상치(outlier)에 강함

**장점:** 직관적 해석, 이상치에 강함
**단점:** 작은 오차와 큰 오차를 동일하게 다룸

---

### 2. MSE (Mean Squared Error, 평균 제곱 오차)
**공식:**

- 오차를 제곱하여 평균낸 값
- 큰 오차를 강조하여 학습 가능
- 값이 작을수록 모델 성능이 좋음

**장점:** 최적화 용이, 큰 오차 강조
**단점:** 이상치에 민감, 단위 해석 어려움

---

### 3. RMSE (Root Mean Squared Error, 평균 제곱근 오차)
**공식:**

- MSE의 단점을 보완하여 실제 값과 동일한 단위로 변환
- 값이 작을수록 모델 성능이 좋음

**장점:** 실제 단위와 일치하여 해석이 용이
**단점:** 이상치에 민감

---

### 4. MAPE (Mean Absolute Percentage Error, 평균 절대 백분율 오차)
**공식:**

- 예측 오차를 백분율(%)로 나타냄
- 값이 작을수록 모델 성능이 좋음

**장점:** 단위 없음(비교 가능), 직관적 해석 가능
**단점:** 실제 값이 0에 가까우면 오류 발생

---

### 5. R² Score (결정 계수)
**공식:**

- 모델이 데이터를 얼마나 잘 설명하는지를 나타냄
- 1에 가까울수록 좋은 모델

**장점:** 모델의 설명력을 쉽게 확인 가능
**단점:** 과적합 발생 가능, 비선형 관계에 약함

---

### 지표 비교 및 선택 가이드
| 지표  | 설명 | 해석 | 장점 | 단점 | 주요 사용 사례 |
|---|---|---|---|---|---|
| **MAE** | 평균 절대 오차 | 값이 작을수록 좋음 | 해석 직관적, 이상치에 강함 | 작은 오차와 큰 오차 동일 취급 | 일반적인 오차 분석 |
| **MSE** | 평균 제곱 오차 | 값이 작을수록 좋음 | 최적화 쉽고, 큰 오차 강조 | 이상치에 민감, 단위 문제 | 모델 학습 |
| **RMSE** | 평균 제곱근 오차 | 값이 작을수록 좋음 | 실제 값과 같은 단위 | 이상치에 민감 | 회귀 모델 평가 |
| **MAPE** | 평균 절대 백분율 오차 | 값이 작을수록 좋음 (%) | 비교 가능, 직관적 해석 | 0 근처 값 문제 | 비즈니스 모델 평가 |
| **R² Score** | 결정 계수 | 1에 가까울수록 좋음 | 모델 성능 파악 가능 | 과적합 가능성 | 모델 설명력 평가 |

---

### 정리
- **MAE**: 절대 오차 (이상치에 강함)
- **MSE**: 제곱 오차 (큰 오차 강조)
- **RMSE**: MSE 보완, 실제 단위 유지
- **MAPE**: 오차 비율 (%) 측정
- **R² Score**: 모델
'''
#

#학습의 모델 
#예측 전제조건 훈련
#첫번째 실제값 - 예측값 차이 표현의 묘미 
#mae ,mse ,mape, 

#해결 2] x,y 데이터 값을  data= {'x':[], 'y':[]}

#해결 3] df 판다스로 bar 모양의 plt

#해결4 ] 학습모델 새로 추가  LinearRegression 연속적인 숫자데이터. 모델 생성 ,fit(), predict() 후 accuracy 측정

# 행렬을 바꿔주는 방법

# DataFrame 값 데이터 값 출력 확인
print()
print()
