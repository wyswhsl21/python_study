# import matplotlib.pyplot as plt        # 첫번째
# from  matplotlib import pyplot as plt  # 두번째
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

# 음수표기 관리
import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import pandas as pd
import numpy as np
import seaborn as sns 
import time
#--------------------------------------------------------------------------------------------

#사이킷런(scikit-learn) 라이브러리 임포트
# ----------------------------------------------------------------------------------------------
# X1, X2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01),
#                      np.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))


my_array = np.arange(0.1,1,0.1)
my_array = np.array([1,2,3,2,1,4,5,4,6,5])
unique = np.unique(my_array)
print(my_array)
print(unique)
print()
x = np.linspace(1,10,10)
y = np.linspace(11,20,10)
X1 , X2 = np.meshgrid(x, y)
# plt.scatter(X1, X2)
plt.scatter(x,y)
plt.grid()
plt.show()

A = np.array([1,2,9,4,5,6])
print(A)
print('shape 확인',A.shape) #



#np.newaxis 괄호없음
#flatten() , ravel()
# meshgrid, linspace , unique , array, arange, max, min 
print()
#해결 1] 3행 * 2열
print(A.reshape(3,2))

#해결 2] 3행 *2 열을 다시 원복 하기
A.ravel()
print(A)
A = np.array([1,2,3,4,5,6])
print(A.flatten())
print(A[:,np.newaxis].shape)




















print()
print()









print()
print()
