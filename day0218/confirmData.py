import pandas as pd

path = './data/health.csv'

df = pd.read_csv(path)

print(df.info())  #데이터 살펴보기

print(df.head(1)) # 첫 n 행을 출력, 인자에 n 을 넣으면 n 행 출력

print(df.describe()) #데이터 프레임 요약 통계량 보기

weight = df['WEIGHT']
print()
print(weight)
print()

consecutive_columns = df[['WEIGHT','WAIST','HEMOGLOBIN']]
df1 = df[df['HEIGHT'] >= 180]
print(consecutive_columns)

print()
print(df1)

print()
df2= df[df['WEIGHT'].isin([70,60,85])]
print(df2)
print()
height = df.groupby('HEIGHT')
