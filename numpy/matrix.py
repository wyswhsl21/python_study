# 
import numpy as np

# 3x3 항등행렬 생성
identify_matrix = np.identity(3)
print('3x3 항등행렬:')
print(identify_matrix)

A = np.array([[2, 3],
              [1, 4]])

A_inverse = np.linalg.inv(A) #A 의 역행렬 계산

print("행렬 A의 역행렬 : ")
print(A_inverse)

