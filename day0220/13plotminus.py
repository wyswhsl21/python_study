import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
from matplotlib import font_manager
from matplotlib.collections import EventCollection

matplotlib.rc('axes',unicode_minus=False)
matplotlib.rcParams['axes.unicode_minus']=False
font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

# font_name= font_manager.font_family_aliases('경로').get_name()

x = np.linspace(-np.pi,np.pi,1000)
print(x)
y1=np.cos(x)
y2=np.sin(x)

plt.plot(x,y1)
plt.plot(x,y2)

plt.show()