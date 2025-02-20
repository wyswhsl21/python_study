import math
import numpy as np
import time as time



print(np.zeros(10))
print(np.ones(10))
print()

print(np.zeros([4,5]))
print()
print(np.ones([4,5]))

print()
# 78 숫자를 4행 6열
z=np.full((4,6),0)
print(z)
print()

z=np.full((4,6),78)
print(z)
print()

#전치행렬 만들어주는 eye함수
z=np.eye(4,6)
print(z)