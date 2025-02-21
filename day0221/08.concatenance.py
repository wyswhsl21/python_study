import numpy as np

c = np.array(([1, 2, 3], [7, 8, 9]))  # #2행 3열

print('변형', np.transpose(c))
print()
print('변형', c.T)
print()

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

ret1 = np.concatenate((a, b), axis=0)
ret2 = np.concatenate((a, b.T), axis=1)
print(ret1)
print(ret2)

import math
import numpy as np
import time as time

print()
#에러  a = np.array(  [1,2], [3,4]  ) # Field elements must be 2- or 3-tuples, got '3'
x = np.array([1, 2, 3])  #1행3열
y = np.array([7, 8, 9])  #1행3열

print(np.vstack((x, y)))  #[ [1 2 3]  [7 8 9] ]  위 아래
print()
print(np.hstack((x, y)))  #[  1 2 3 7 8 9 ]   왼쪽에서 오른쪽

# vstack 은 열을 기준으로 쪼개서 쌓는거고     #12
#                                          #34

# 12
# hstack 은 행을 기준으로 1,2,5,6 3,4,7,8

print()
print(np.concatenate((x, y), axis=1))
