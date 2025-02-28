
import pandas as pd
import numpy as np


#-----------------------------------------------------------------------------------------------------
# 통계, 수학 2차원부터 X대문자 사용, x소문자사용도 전혀 에러 없음

X = [ [ 1, 2, 3 ],   [ 3, 4, 5 ],   [ 5, 6, 7 ],   [ 7, 8, 9 ] ]
y = [ 0, 1, 0, 1]  
from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test  = train_test_split( X, y, test_size=0.2) 

from sklearn.impute  import SimpleImputer
# imputer = SimpleImputer(strategy='most_frequent') 
# data  = imputer.fit_transform(data)

from sklearn.preprocessing import MinMaxScaler, StandardScaler
data = [ [1, 2, 3, 4, 5],  [4, 5, 6, 7, 8],  [7, 8, 9, 10, 11] ]
data = np.array(data)
print(data)
print()















print()
print()