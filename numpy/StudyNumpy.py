import numpy as np

# 1차원 배열 생성 하는 방법

a = np.array([1,2,3])

# 2차원 배열 생성
b = np.array([[1,2,3],[4,5,6]])

# 3차원 배열 생성

c = np.array([[[1,2],[3,4],[5,6],[7,8]]])
# print(f'{a}\n{b}\n{c}')

# 배열의 크기를 확인 방법은 shape 이용

print(a.shape)
print(b.shape)
print(c.shape)

c=a+b 

