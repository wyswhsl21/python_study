import numpy as np

import time


def myTest(x, y):
    ret = x * 10 + y
    return ret


print(myTest(3, 7))
print(np.fromfunction(myTest, (3, 7), dtype=int))

print()
print(myTest(5, 6))
