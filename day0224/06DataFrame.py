import pandas as pd

int_values = [2021, 2019, 2005, 2014, 2025]
text_values = ['길동', '희동', '둘리', '라미', '영우']
float_values = [1.2, 4.5, 8.1, 7.5, 3.4]
df = pd.DataFrame({
    "year": int_values, 
    "name": text_values,
    "point": float_values })

print(df)
print()
print(df.info())
print()
# print(df.describe()) #실수
# print()

#06DataFrame.py문서
'''
 <class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   year    5 non-null      int64
 1   name    5 non-null      object
 2   point   5 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 252.0+ bytes
'''







print()
print()
