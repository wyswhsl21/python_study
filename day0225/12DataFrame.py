import pandas as pd
import numpy as np 

# 판다스에서 연산가능 확인 
student1 = pd.Series( {'kor': 80,   'eng': 50, 'mat': 90} )
student2 = pd.Series( {'kor': None,   'eng': 70, 'mat': 50})
# student2 = pd.Series( {'kor': np.nan,   'eng': 70, 'mat': 50})

plus = student1 + student2
minus = student1 - student2
mul = student1 * student2
div = student1 / student2


df = pd.DataFrame( [plus, minus ,mul,div],  index = ['더함','빼기','곱함','나눔'])
print(df)
# EDA(Exploratory Data Analysis, 탐색적 데이터 분석)















print()
print()
