import pandas as pd
import time
path ='./data/emp.csv'

# 해결 1 판다스 이용해서 path 문자열
df = pd.read_csv(path,encoding='euc-kr')

df_pay = df.query('Pay == 450')
print(df_pay)

print('\nloc[]추출')
print(df.loc[0:4,:])
print('-' * 30)


print('\niloc[]추출')
print(df.iloc[0:4,:])
print('-' * 30)



print()
