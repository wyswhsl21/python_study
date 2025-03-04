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
# OpenCV = Open Source Computer Vision 라이브러리 
# pip install opencv-python 설치

#아이리스 붓꽃 iris 3종류 세토사 , 버시킬러, 버지니카
#sepal :꽃받침 , petal: 꽃잎
iris = sns.load_dataset('iris')
print(iris)
print()
print(iris.info())
# 
species = iris['species'].unique()
print('품종의 unique 결과',species) #['setosa' 'versicolor' 'virginica']

sepal_length_list = [iris[iris['species'] == s] ['sepal_width'] for s in species]
print('sepal_length_list',sepal_length_list)
print('품종의 sepal',)
plt.figure(figsize=(12,7))
sns.boxplot(x='species',y='sepal_length',data=iris,palette='Set1') #virginica 길이
# sns.boxplot(x='species',y='sepal_width',data=iris) #setosa 폭 높죠
# plt.boxplot(sepal_length_list,labels=species)
plt.title('세토사 버시컬러 버지니카 붓꽃 떡받침')
plt.show()



# sepal_length  sepal_width  petal_length  petal_width  species





print()
print()
