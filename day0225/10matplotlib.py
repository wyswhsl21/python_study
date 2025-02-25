# import matplotlib
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
import time
import platform
print('현재 컴퓨터 os플랫폼 확인',platform.system())
#-----------------------------------------------------------------------------------------------------
# x = [ 1, 2, 3, 4, 5]
x = [ 'a', 'b',	'c', 'd', 'e']
y = [2, 3, 5,	7,	11]
y1	= [2, 3, 5,	7,	11]
y2	= [1, 4, 6,	8,	10]

plt.plot(x,y)
plt.title('line plot test')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.savefig('./images/testplot.png')
print('./images/testplot.png 파일저장 성공했습니다 ')
plt.show()


'''
해결1] 큰제목, x제목, y제목
해결2] 서브플롯  plt.plot(x,y) 라인차트 
plot(), subplot(), scatter(), savefig()
'''































print()
print()