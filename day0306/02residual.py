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
#--------------------------------------------------------------------------------------------
# 해결 02 잔차
x =  [13, 19, 16, 14, 15, 14]
y =  [40, 83, 62, 48, 58, 43]

a,b = np.polyfit(x,y,1) # 선형회귀 추세 미래 예측
print(f'기울기 ={a}, 절편 = {b}')
# print()
print('*'* 50)

#해결 2] x,y 데이터 값을  data= {'x':[], 'y':[]}
df = pd.DataFrame({'x':[13, 19, 16, 14, 15, 14],'y':[40, 83, 62, 48, 58, 43]})
print(df)
print('*'* 50)
#해결 3] df 판다스로 bar 모양의 plt
# df.plot(kind='bar',x='x',y='y',legend=False,color='orange')
plt.xlabel('xData')
plt.ylabel('yData')
plt.title('잔차 오차 작업 데이터')



#해결4 ] 학습모델 새로 추가  LinearRegression 연속적인 숫자데이터. 모델 생성 ,fit(), predict() 후 accuracy 측정
print(f'선형회귀 시작 ')
lr = LinearRegression()
# print("df 판다스 df['x'] shape",type(df['x'])) #df 판다스 df['x'] shape <class 'pandas.core.series.Series'>
# print("df 판다스 df['x'] shape",df['x'].shape) #df 판다스 df['x'] shape (6,)

# 행렬을 바꿔주는 방법 판다스의 toFrame() ,
#  x_reshaped = df['x'].values[:, np.newaxis] np.newaxis 는 열을 기준으로 직접 차원 추가할때 만드는 방법
# reshaped = df[['x]] 가장 쉬운 방법
reshape_x = df['x'].values.reshape(-1,1) # -1 의 의미 행렬 자동 계산해줌 1은 몇 차원으로 만들건지.
# print(reshape_x,reshape_x.shape)
print('- ' * 40)
lr.fit(reshape_x,df['y']) #fit 은 1차원 이상부터 할수있음.
print(f'가중치 w',lr.coef_)
print(f'편향 b',lr.intercept_)
print()
#해결 5] 판다스의 df['x'] shape 변형 해줘야 함.

y_pred = lr.predict(reshape_x)
print('예측', y_pred)
print('실제 데이터\n', df)

# DataFrame 값 데이터 값 출력 확인

plt.plot(df['x'],y_pred,color='green',label='predict') #예측
plt.scatter(df['x'],df['y'],color='red',label='actual') #실제값

for i,v in enumerate(df['x']):
    plt.text(v,df['y'][i],f'({df["x"][i]}, {df["y"][i]})',fontsize=12,color='hotpink')
    hr ='left'
    va='top'

plt.grid(axis='both',linestyle='--',alpha=0.8)

plt.legend()
plt.show()

print()
print('잔차 처리 계산')



#해결 7 실제값 - 예측값 = 잔차값 절대화 
resi_sum = 0  # 초기화

# 실제값 - 예측값 = 잔차값 (절대값 적용)
for i, v in enumerate(df['x']):
    residual = df['y'][i] - y_pred[i]  # 잔차 계산
    abs_residual = abs(residual)  # 절대값 적용

    print(f'{df["y"][i]:.0f} - {y_pred[i]:.2f} = {residual:.2f}')
    
    resi_sum += abs_residual  # 절대 잔차 합산

# 잔차 합계 출력
print(f'잔차 합계 = {resi_sum:.2f}')

# 평균 절대 잔차 (Mean Absolute Error, MAE)
total = resi_sum / len(df['x'])
print('- ' * 40)
print(f'평균 절대 잔차 = {total:.2f}')

from sklearn.metrics import mean_absolute_error
print('mae 결과' , mean_absolute_error(y,y_pred))

# 해결 9] 잔차 ** 2 처리후 / sqrt() 적용해 출력 
# RSS = Residual Sum of Square
residuals = df['y']-y_pred
RSSTotal = (residuals ** 2).sum()
sqrt_residuals = np.sqrt(residuals)
print('sqrt_sum =',RSSTotal)
print("RSSTotal/6 =", RSSTotal/ 6)
print("RSSTotal/6 sqrt 적용 =", np.sqrt(RSSTotal/ 6))

from sklearn.metrics import mean_squared_error
print('mse 결과 ', mean_squared_error(y,y_pred)) #rssTotal 에 제곱근 적용하지 않은것과 같음.
from sklearn.metrics import root_mean_squared_error
print('rmse 결과 ', root_mean_squared_error(y,y_pred)) # rssTotal /6 에 제곱근 적용 한게 같다.

'''
✔ R² Score는 모델이 데이터를 얼마나 잘 설명하는지 측정하는 지표
✔ 1.0에 가까울수록 좋고, 0.0이면 평균값과 동일한 성능
✔ r2_score(y_actual, y_pred)로 간단하게 계산 가능
✔ R² < 0이면 모델이 데이터를 설명하지 못함 → 모델 개선 필요

결정계수 공식 = 1-(잔차 합/총 변동 합)
잔차합 =  np.sum((df['y']-y_pred)**2)
변동합 =  np.sum((df['y']-y_mean)**2)

'''
from sklearn.metrics import r2_score

print('r2_score 결과 ', r2_score(y,y_pred))
y_mean = np.mean(df['y'])
res = np.sum((df['y']-y_pred)**2)
tot = np.sum((df['y']-y_mean)**2)
r2_sc = 1-(res/tot)
print('r2_sc =',r2_sc)




print()
print()
