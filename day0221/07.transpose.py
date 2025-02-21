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
