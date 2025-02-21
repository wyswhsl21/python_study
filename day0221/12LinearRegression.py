import matplotlib.pyplot as plt
from matplotlib  import font_manager, rc
font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import numpy as np

# 단계1 ]  총합계,평균 구하기
x = [2, 4, 6, 8, 10]         #총합계 30/5   평균 6시간
y = [81, 93, 91, 97, 98]     #총합계 460/5  평균 92점

su = np.polyfit(x,y,1)
print('선형회귀 ', su) # 권장 결과  [1.9  80.6]
print()

# 단계2] 선형회귀 공식 y = W가중치*시간 + b편향
y_pred = np.array(x)*su[0] + su[1] 
print( y_pred)  #예측값 [84.4  88.2   92.  95.8   99.6]
print()

plt.plot(x, y_pred, color='hotpink')   #예상=예측값
plt.scatter(x, y, color='red')   #실제값
plt.plot(x,y)  #line기본모양

for i,v in enumerate(x):
    plt.text(v, y[i], y[i], fontsize=12,  color='blue',  
    horizontalalignment='left',
    verticalalignment='bottom'
    )
plt.title('시간투자 성적점수 선형회귀 EST')
plt.xlabel('공부시간 EST')
plt.ylabel('시험점수 EST')

plt.show()
print('시각화 작업 확인 ok ')









'''
단위행렬(Unit matrix): np.eye(n)
영행렬(Zaro matrix): np.zeros((m, n))
대각행렬(Diagonal matrix): np.diag(x)
전치행렬(Transpose matrix): np.T, np.transpose(a)
내적(Dot product, inner product): np.dot(a, b)
대각합(trace): np.trace(x)
행렬식(Matrix Determinant): np.linalg.det(x)
역행렬(Inverse of a matrix): np.linalg.inv(x)
최소자승 해 풀기: m, c = np.linalg.lstsq(A, y, rcond=None)  선형회귀공식과 관련 소숫점 8자릿수

고유값(Eigenvalue), 고유vector(Eigenvector): w, v = np.linalg.eig(x)
특잇값 분해(Singular Value Decomposition): u, s, vh = np.linalg.svd(A)
연립방정식 해 풀기: np.linalg.solve(a, b)


# 최소자승 해 풀기: m, c = np.linalg.lstsq(A, y, rcond=None)  선형회귀공식과 관련 소숫점 8자릿수
A = np.vstack( [x, np.ones(len(x))] ).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
print(round(m,2), round(c,2)) #1.8999999999999921      80.59999999999997
print()

'''













print()
print()