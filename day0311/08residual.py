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
# 해결1] 리스트 넘피이용해서 가중치, 바이어스 구하기  np.polyfit( ) 선형회귀 추세 미래예측
# x =  [13, 19, 16, 14, 15, 14]
# y =  [40, 83, 62, 48, 58, 43]
# ret = np.polyfit(x, y, 1)
# print('넘피 가중치w 편향b 결과 ', ret)
# print('넘피 가중치 =', ret[0], '  넘피편향 =',  ret[1])
# print()
# print('- ' * 30)

# 해결2] x,y데이터값을  data = { 'x':[], 'y':[ ] } 딕트구조를 판다스의 데이터프레임
data = {  'x':[13, 19, 16, 14, 15, 14] , 
          'y':[40, 83, 62, 48, 58, 43] }

df = pd.DataFrame(data)
# print(df)
# print()

# 해결3] df판다스로  bar모양 그래프 작성   ㅇf.plot( ) ~~ plt.show()
# df.plot(kind='bar', x='x', y='y', color='hotpink')
# plt.title('잔차 오차 작업 데이터 ')
# plt.show()

# 해결4] 학습모델 LinearRegression모델임포트 모델생성(), fit(), predict()
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

lr = LinearRegression() 
# print("df판다스 df['x'] shape ", type(df['x'])) # <class 'pandas.core.series.Series'>
# print("df판다스 df['x'] shape ", df['x'].shape) #  df['x'] shape  (6,)

# 해결5] 판다스의 df['x'] shape변형해줘야 합니다 
# lr.fit(df[['x']], df['y']) #차원승격 가능
x = df['x'].values[ :,  np.newaxis] #차원승격
lr.fit(x, df['y'])
print('가중치w ',lr.coef_ )
print('편향b ', lr.intercept_)
print()

# 해결4연장] 학습모델 LinearRegression모델임포트 모델생성(), fit(), predict()
y_pred = lr.predict(x)
print('예측 데이터 ', y_pred)  
#         [39.78832117 83.75912409 61.77372263 47.11678832 54.44525547 47.11678832] 분홍핑크hotpink
# 'y값' : [40,        83,         62,         48,         58,         43]

y =  [40, 83, 62, 48, 58, 43]
# 해결6]  plt.scatter(원래값) , plt.plot(x, y_pred ), for반복문 plt.text( v,좌표~~~)
plt.scatter(df['x'], df['y'], color='green')
plt.plot(x, y_pred)
for i,v in enumerate(x):
    plt.text(v, y[i], y[i], fontsize=12,  color='blue',  
     horizontalalignment='left',
     verticalalignment='bottom'
   )
# plt.show()
print('- ' * 30 )

# 해결7]   실제값 - 예측값  = 잔차값 절대화, 잔차합계/6 = 1.635 
print()
residuals = data['y'] - y_pred
for i in range(len(residuals)):
    print(data['y'][i] , '-' , np.round(y_pred[i],2) ,'=' , np.round(residuals[i],2))
result = np.sum(np.abs(residuals))/6
print('잔차합계 =', np.sum(np.abs(residuals)))
print('잔차평균 =',result) #잔차평균 1.625
print()
'''
40 - 39.79 = 0.21
83 - 83.76 = -0.76
62 - 61.77 = 0.23
48 - 47.12 = 0.88
58 - 54.45 = 3.55
43 - 47.12 = -4.12
실제-예측값 = 결과값을 절대화abs()적용후  합계  9.75/6 = 잔차평균 1.625 
'''   
# 해결8] 접미사 error 잔차값 mae
from sklearn.metrics import mean_absolute_error
print('mae결과 =', mean_absolute_error(y,y_pred)) #잔차평균 1.625 

# 해결9] RSS = Residula Sum of Square   잔차**2처리 합계/6  sqrt()적용해 출력
# 잔차제곱합/6 =  5.172749391727503   sqrt = 2.2743679103714736 
RSSTotal = (residuals**2).sum()
print('RSSTotal 합계결과 =', RSSTotal)               #RSSTotal 합계결과 = 31.03649635036502
print('RSSTotal/6결과 =', RSSTotal/6)                #5.172749391727503  동일한결과 mean_squared_error
print('RSSTotal/6 sqrt적용 =', np.sqrt(RSSTotal/6))  #2.2743679103714736   동일한결과 root_mean_squared_error(y,y_pred)

from sklearn.metrics import mean_squared_error
print('mse결과 =', mean_squared_error(y,y_pred))      #5.172749391727503 동일한결과 RSSTotal/6

from sklearn.metrics import root_mean_squared_error
print('rmse결과 =', root_mean_squared_error(y,y_pred))  #2.2743679103714736 동일한결과  np.sqrt(RSSTotal/6)

from sklearn.metrics import mean_absolute_percentage_error
print('mape결과 =',  mean_absolute_percentage_error(y,y_pred)) #수작업처리못함 0.03225264741536682

# 해결10] r2_score 역할  # TSS = total sum of squares
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import r2_score
print('r2_score결과 =', r2_score(y,y_pred))   # r2_score결과 = 0.9753156179610034
                                              # 31.03 / 1257.33 = 0.024  1-0.024 = 0.97

print()
TSS = ((df['y'] - df['y'].mean())**2 ).sum()  
print("TSS 합계결과  =", TSS)           # 1257.3333333333333
print('RSSTotal 합계결과 =', RSSTotal)  # 31.03649635036502
print('(RSSTotal/TSS) 결과 =', (RSSTotal/TSS)) # 0.02468438203899657
r2_score = 1 - (RSSTotal/TSS)
print('r2_score결과 =', r2_score)       # 0.9753156179610034 더편하게 값-예측값=잔차를 절대화 합계 

'''
40 - 39.79 = 0.21
83 - 83.76 = -0.76
62 - 61.77 = 0.23
48 - 47.12 = 0.88
58 - 54.45 = 3.55
43 - 47.12 = -4.12
실제-예측값 = 결과값을 절대화abs()적용후  합계  9.75/6 = 잔차평균 1.625 
'''  


print()
print('가중치w ',lr.coef_ )    #가중치대신 coef결정계수 Coefficient of Determination
print('편향b ', lr.intercept_) #편향 bias intercept
print()

















print()
print()
