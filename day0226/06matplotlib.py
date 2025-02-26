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

# --------------------------------------------------------------------------------------
fruits = ['apple', 'blue', 'kiwi', 'mango']
price = [65,135,70,90] #갯수, 가격
colors = ["red", "blue", "green", "orange"]

#해결 1] bar , plot인지 가격 숫자 표시
plt.figure(figsize=(10,5))
plt.bar(fruits,price,color=colors)

# plt.plot(fruits, y_pred, color='hotpink')   #예상=예측값
plt.scatter(fruits, price, color='red')   #실제값
plt.plot(fruits,price,color='red')  #line기본모양
for i,v in enumerate(fruits):
    plt.text(v, price[i]+0.9, price[i], fontsize=10,  color='blue',  
    ha='center',    #ha
    va='bottom'     #va
    )
legend_patches = [mpatches.Patch(color=color, label=fruit) for fruit, color in zip(fruits, colors)]
plt.legend(handles=legend_patches, title="Fruits")
plt.title('과일별 금액')
plt.xlabel('과일 이름')
plt.ylabel('가격')

plt.savefig('./images/fruits.png')
print('./images/fruits.png 저장하였습니다.')
plt.show()


'''
# area = ['서울', '안양', '수원', '일산']
# su1 = [21, 34, 45, 13]
# su2 = [45, 19, 31, 50]
# su3 = [33, 56, 27, 41]
# su4 = [77, 26, 65, 29]



'''