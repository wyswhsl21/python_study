import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


model = LinearRegression()
print('scikit 라이브러 임포트 ok ')
print()


# ModuleNotFoundError: No module named 'sklearn'
# 설치 pip install scikit-learn 