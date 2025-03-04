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
# iris = sns.load_dataset('iris')
# print(iris)
# print()
# print(iris.info())
# # 

# plt.show()
# print('sns 사본의 이용한 데이터 set')
# sepal_length  sepal_width  petal_length  petal_width  species

#데이터셋 dataset sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

iris = load_iris() #첫번째 에러
print(iris)
print()


'''
시본의 dataset Seaborn as sns 이용
'''

