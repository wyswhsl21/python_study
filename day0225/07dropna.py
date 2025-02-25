import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['홍길동', '본인명' ,'고희동', '가나다'] ,
    'Age': [ 24, np.nan,  17,  20 ]
})

print(df)
print()

df['Age'] = df['Age'].fillna(df["Age"].mean()).astype(int)
print(df)
print()


df['city'] = [ '서울' , '제주',  '독도', '수원' ]
print(df)
print()

df = df.rename(columns={'Age':'Years'})
print(df)
print()

# df = df.drop(columns={'city'}) #df['city'] 정답
df = df.drop(columns=['city'])  #df['city'] 가능 
print(df)
print()

'''
fillna(), rename(), drop()
해결1] 나이 Age  NaN형태  나이의 평균값으로 채우기
해결2] 열추가 city '서울' , '제주',  '독도', '수원' 
해결3] Age필드명을  Years 이름변경
해결4] city열 삭제
int()  round()  str() type()  astype()  
'''




































print()
print()