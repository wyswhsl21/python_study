import numpy as np
import time

dt = np.arange(1, 11)
print(dt)

np.random.shuffle(dt)  #shuffle 하면 원본의값이 무작위로 섞이는데

print(dt)
print('np.random.shuffle(dt) testing....')
data = np.arange(1, 11)
print(data)
print(np.random.permutation(data))  # permutation 을 사용하면 원본의값을 유지하면서 섞을 수 있다.
print(data)
