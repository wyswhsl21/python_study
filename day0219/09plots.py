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
x = ['aa','bb','cc','dd','ee']
y= [1501,444,534252,423124,312132]

fig,ax = plt.subplots(x,y)
ax.plot(x,y)


plt.show()