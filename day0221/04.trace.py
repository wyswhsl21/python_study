import numpy as np
import time

y = np.arange(16).reshape(4, 4)  #4행 4열
print(y)
print(f'trace 결과 \n{np.trace(y)}')

print()

time.sleep(1)

z = np.arange(27).reshape(3, 3, 3)
print(z)
print(f' 두번째 trace {np.trace(z)}')
