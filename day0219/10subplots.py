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




# Plot a straight diagonal line with ticked style path
x = np.linspace(0,2*np.pi,200)
y= np.sin(x)

y1 = [20,50,74,30]  #y축값
y2 = [50,90,30]     #y축값
y3 = np.random.randint(5,35,5) #y축값
y4 = [30,90,10,60,80]



fig,ax = plt.subplots(2,2,figsize=(10,10),) # figsize 가로 , 세로 , share 옵션 x축을 share 한다는 의미
ax[0,0].bar(['a','b','c','d'],y1)
ax[0,0].set_title('알파벳 친구')


ax[0,1].scatter(['y2a','y2b','y2c'],y2)
ax[0,1].set_title('y값들')


ax[1,0].plot(['할리','밀리','칠리','칠가이','킹킹'],y3)
ax[1,0].set_title('할리갈리')


ax[1,1].bar(['e','f','g','h','i'],y4)
ax[1,1].set_title('e~i 까지 값')
fig.suptitle('2025년 ESTsoft 회사 고객동향')



plt.show()