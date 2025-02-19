import numpy as np
import matplotlib.pyplot as plt
#음수표기 관련
import matplotlib
from matplotlib import rc
from matplotlib import font_manager
import matplotlib as mpl
import numpy as np

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)


x = np.random.randn(10000)
plt.hist(x,bins=20,color='orange')
plt.title('chart')
plt.show()

name = ['재우','수연','태경','규홍']
data = [1000,2500,5000,10000]

# fig,ax = plt.subplots() #subplots 는 인자 두개를 받음
# ax.bar(name,data,color='r')
plt.bar(name,data,color='b')
plt.show()

name = ['a','b','c','d']
data = [20,40,60,75]
plt.scatter(name,data,s=90,c='red',marker='p')
plt.title('scatter test 그래프')
plt.show()

