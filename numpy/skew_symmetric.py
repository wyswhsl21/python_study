# skew-symmetric Matrix 반대칭 행렬

import numpy as np
# 반대칭행렬
A= np.array([[0,2,-3],[-2,0,5],[3,-5,0]])


A_transpose = A.T

skew_symmetric_matrix = -A_transpose

print("Given Matrix A:")
print(A)

print("\nTranspose of Matrix A:")
print(A_transpose)