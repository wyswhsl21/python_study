# 대각행렬
import numpy as np
'''
대각행렬은 대각선 상의 원소 이외에 원소가 모두 0인 행렬 대각 행렬은 
주로 다양한 수학적 연산과 변환 표현 사용
'''

symmetric_matrix = np.array([[1,2,3],[2,4,5],[3,5,6]])

print("대칭행렬")
print(symmetric_matrix)

#대각행렬 생성

diagonal_matrix = np.diag([2,5,8])
print('대각행렬')
print(diagonal_matrix)