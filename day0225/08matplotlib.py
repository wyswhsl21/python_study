import matplotlib
import matplotlib.pyplot as plt        # 첫번째
from  matplotlib import pyplot as plt  # 두번째
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)


# --------------------------------------------------------------------------------------------------------------------
x = [1, 2, 3, 4, 5] 
y = [2, 3, 5, 7, 11]
plt.plot(x,y)
plt.title('')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
print('matplotlib test Ok')