import matplotlib
import matplotlib.pyplot as plt       # 첫번째
from  matplotlib import pyplot as plt  # 두번째
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc
import time
import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)


# --------------------------------------------------------------------------------------------------------------------
# x = [1, 2, 3, 4, 5] 
x = ['a', 'b', 'c', 'd', 'e'] 
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]
plt.subplot(2,1,1)
plt.plot(x,y1,'r')
plt.title('line plot y1')

plt.subplot(2,1,2)
plt.plot(x,y2,'g')
plt.title('line plot y2')

plt.tight_layout() #타이틀 간격 자동 조정

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
print('matplotlib test Ok')



time.sleep(1)

x = [1, 2, 3, 4, 5] 
y = [2, 3, 5, 7, 11]
plt.scatter(x,y)
plt.title('scatter test')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()