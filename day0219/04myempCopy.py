import pandas as pd
import time
path ='./data/emp.csv'

# 해결 1 판다스 이용해서 path 문자열
df = pd.read_csv(path,encoding='euc-kr')

df_pay = df.query('Pay == 450')
print(df_pay)

print('\nloc[]추출') #loc 는 행 번호 기준으로 접근한다.
print(df.loc[0:4,:])
print('-' * 30)


print('\niloc[]추출') #iloc 는 인덱스 기준으로 접근
print(df.iloc[0:4,:])
print('-' * 30)




print(df)
delete_df = df.query('Pay >=400') #쿼리를 이용한 방법

dfCopy = df
delete_data = dfCopy[dfCopy['Pay'] >= 400].index
remove = dfCopy.drop(delete_data)
dfCopy.drop(delete_df.index, inplace=True)
# dfCopy.drop(delete_data)
pay_drop_emp = pd.DataFrame(dfCopy)
pay_drop_emp.to_csv('./data/pay_drop_emp.csv')
pay_drop_emp2 = pd.DataFrame(remove)
pay_drop_emp2.to_csv('./data/pay_drop_emp2.csv')
print('./data/pay_drop_emp.csv 저장 성공했습니다.')


time.sleep(1) #1초 지연시간
