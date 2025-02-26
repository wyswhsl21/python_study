import matplotlib
import matplotlib.pyplot as plt        # 첫번째
from  matplotlib import pyplot as plt  # 두번째
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc
import seaborn as sns
import matplotlib.patches as mpatches
# 음수표기 관리
import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import pandas as pd
import numpy as np
import time
import seaborn as sns

# --------------------------------------------------------------------------------------

sns.set_theme()
tips = sns.load_dataset('tips')
corr = tips.corr() #피어슨, 스피어만, 켄달
print(corr)
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.show()
print()
# sns.relplot(data=tips,x='total_bill',y='tip',col='time',hue='smoker',style='smoker',size='size')
# sns.displot(data=tips, x="total_bill", col="time", kde=True)
# sns.catplot(data=tips, kind="bar", x="day", y="total_bill", hue="smoker")
# print(tips) #total_bill   tip     sex smoker   day    time  size

plt.show()


penguins =sns.load_dataset('penguins') 
# print(penguins) #species     island  bill_length_mm  ...  flipper_length_mm  body_mass_g     sex

# sns.jointplot(data=penguins, x='flipper_length_mm', y='bill_length_mm',hue='island')
# sns.pairplot(data=penguins, hue="species")
plt.show()