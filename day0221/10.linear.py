import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(
    fname='C:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)
import numpy as np

#단계1 ]  총합계,평균 구하기
x = [2, 4, 6, 8, 10]  #총합계 30 /5   평균 6시간
y = [81, 93, 91, 97, 98]  #총합계 460 /5  평균 92점
su = np.polyfit(x, y, 1)
print(su)  # 결과출력 [1.9 가중치 80.6분산]
print()

#단계2] 선형회귀 공식 y = W가중치 x 시간 + b편향
y_pred = np.array(x) * su[0] + su[1]
print(y_pred)  #예측값 [84.4 88.2 92.  95.8 99.6]
print()

# 행렬 = matrix
# 넘피Numpy에서 자주사용 되는 선형대수 함수
# matrix는 행렬
# 단위행렬(Unit matrix): np.eye(n)
# 영행렬(Zaro matrix): np.zero((m, n))
# 대각행렬(Diagonal matrix): np.diag(x)
# 전치행렬(Transpose matrix): np.T, np.transpose(a)
# 내적(Dot product, inner product): np.dot(a, b)
# 대각합(trace): np.trace(x)
# 행렬식(Matrix Determinant): np.linalg.det(x)
# 역행렬(Inverse of a matrix): np.linalg.inv(x)
# 고유값(Eigenvalue), 고유백터(Eigenvector): w, v = np.linalg.eig(x)
# 특잇값 분해(Singular Value Decomposition): u, s, vh = np.linalg.svd(A)
# 연립방정식 해 풀기: np.linalg.solve(a, b)
# 최소자승 해 풀기: m, c = np.linalg.lstsq(A, y, rcond=None)
