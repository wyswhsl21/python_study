import matplotlib.pyplot as plt
from matplotlib  import font_manager, rc
font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import numpy as np

# 단계1 ]  총합계,평균 구하기
x = [2, 4, 6, 8, 10]         #총합계 30/5   평균 6시간
y = [81, 93, 91, 97, 98]     #총합계 460/5  평균 92점
# 가장쉽게 x시간, y점수 출력, 총점, 평균, 최대, 최소, 빈도수 처리후 끝


su = np.polyfit(x,y,1)
print('선형회귀 ', su) # 권장 결과  [1.9  80.6]   
print()

# 단계2] 선형회귀 공식 y = W가중치*시간 + b편향   
y_pred = np.array(x)*su[0] + su[1] 
print( y_pred)  #예측값 [84.4  88.2   92.  95.8   99.6]
print()

# plt.plot(x, y_pred, color='hotpink')   #예상=예측값
# plt.scatter(x, y, color='red')   #실제값
# plt.plot(x,y)  #line기본모양

# for i,v in enumerate(x):
#     plt.text(v, y[i], y[i], fontsize=12,  color='blue',  
#     horizontalalignment='left',
#     verticalalignment='bottom'
#     )
# plt.title('시간투자 성적점수 선형회귀 EST')
# plt.xlabel('공부시간 EST')
# plt.ylabel('시험점수 EST')
# plt.show()



print('시각화 작업 확인 ok ')

































print()
print()