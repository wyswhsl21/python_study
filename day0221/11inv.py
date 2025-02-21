import numpy as np

# 역행렬(Inverse of a matrix): np.linalg.inv(x)
a = np.array([[1, 2], [3, 4]])
print(a)  # [1, 2], [3, 4]
print()

ret = np.linalg.det(a)
print(ret)  # -2.0000000000000004
print(round(ret, 3))  #-2.000
print(np.abs(ret))  #양수
'''
 [1 , 2]
 [3 , 4]
 대각 1*4 - 2*3   
 # 행렬식(Matrix Determinant): np.linalg.det(x) 
'''

# 역행렬(Inverse of a matrix): np.linalg.inv(x)
a = np.array([[1, 2], [3, 4]])
ret = np.linalg.inv(a)
print(a)  # [1, 2], [3, 4]
print()
print(ret)
'''
# 행렬 = matrix
# 넘피Numpy에서 자주사용 되는 선형대수 함수
# matrix는 행렬
단위행렬(Unit matrix): np.eye(n)
영행렬(Zaro matrix): np.zeros((m, n))
대각행렬(Diagonal matrix): np.diag(x)
전치행렬(Transpose matrix): np.T, np.transpose(a)
내적(Dot product, inner product): np.dot(a, b)
대각합(trace): np.trace(x)
행렬식(Matrix Determinant): np.linalg.det(x)
역행렬(Inverse of a matrix): np.linalg.inv(x)
고유값(Eigenvalue), 고유vector(Eigenvector): w, v = np.linalg.eig(x)
특잇값 분해(Singular Value Decomposition): u, s, vh = np.linalg.svd(A)
연립방정식 해 풀기: np.linalg.solve(a, b)
최소자승 해 풀기: m, c = np.linalg.lstsq(A, y, rcond=None)
'''

print()
