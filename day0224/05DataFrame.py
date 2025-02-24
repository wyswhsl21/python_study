import pandas as pd

int_values = [1, 2, 3, 4, 5]
text_values = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
float_values = [0.0, 0.25, 0.5, 0.75, 1.0]
df = pd.DataFrame({
    "int_col": int_values, 
    "text_col": text_values,
    "float_col": float_values })

print(df)
print()
print(df.info())
print()
print(df.describe()) #실수
print()
'''
   int_col text_col  float_col
0        1    alpha       0.00
1        2     beta       0.25
2        3    gamma       0.50
3        4    delta       0.75
4        5  epsilon       1.00

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   int_col    5 non-null      int64
 1   text_col   5 non-null      object
 2   float_col  5 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 252.0+ bytes
None

        int_col  float_col
count  5.000000   5.000000
mean   3.000000   0.500000
std    1.581139   0.395285
min    1.000000   0.000000
25%    2.000000   0.250000
50%    3.000000   0.500000
75%    4.000000   0.750000
max    5.000000   1.000000
'''







print()
print()
