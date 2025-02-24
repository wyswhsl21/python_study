import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

print('판다스 버젼 ', pd.__version__)
print('넘피 버젼 ', np.__version__)
print()

# scikit 머신러닝 학습이론에서 아래처럼 에러 나오면 
# ModuleNotFoundError: No module named 'sklearn'
# 본인작업폴더\day0224>  pip install scikit-learn 