import numpy as np
import time

x = np.array([[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [11, 12, 13, 14, 15, 16],
              [76, 75, 74, 73, 72, 71], [86, 85, 84, 83, 82, 81],
              [96, 95, 94, 93, 92, 91]])

print(x)
print(f'np.diag 결과', np.diag(x))
