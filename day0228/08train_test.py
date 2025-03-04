import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
#-----------------------------------------------------------------------------------------------------
# 통계, 수학 2차원부터 X대문자 사용, x소문자사용도 전혀 에러 없음
X = [
   [ 1, 2, 3 ],   [ 3, 4, 5 ],
   [ 5, 6, 7 ],   [ 7, 8, 9 ]
 ]
y = [ 0, 1, 0, 1]  
print('train_test분리전')
print(X) # [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]
print(y) # [0, 1, 0, 1]
print('- ' * 30)
print()
X_train, X_test, y_train, y_test  = train_test_split( X, y, test_size=0.2)
print('train X데이터 ',X_train)
print('train y데이터 ',y_train)
print()
print('test X데이터 ',X_test)
print('test y데이터 ',y_test)