import pandas as pd


fname ='./data/emp.csv'

emp = pd.read_csv(fname,encoding='cp949')
print(emp)
print()

print(emp['Name']) #Name 열 필드 추출
print()
print(emp.loc[2])

print(emp.loc[2:5,'Name':'Pay'])
print()

print('2시작행:5끝행 ,Name열 :Pay열')
print(emp.loc[2:5,'Name':'Pay']) # loc [시작:5,'시작열':'끝열']
print()



print(emp.loc[:,'Name':'Pay']) # loc [:,'시작열':'끝열'] 모든행
print()