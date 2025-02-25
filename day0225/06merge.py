import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'ID':[1111,2222,3333,7777],
    'Name':['고희동','홍길동','봄여름','가을씨']
})
df2 = pd.DataFrame({
    'ID':[1111,2222,3333,9999],
    'Name':['서울','제주도','인천','구구구구']
})

print('\n 간단한 머지 테스트')
df_merge = pd.merge(df1,df2,on ='ID')

print(df_merge)
print()
print('\n 간단한 concat 테스트')
df_concat = pd.concat([df1,df2],axis=1) # axis 1 은 열기준 axis 는 행기준
print(df_concat)

'''
merge(),concat()
# fillna(), rename(), drop()
# 해결1] 나이 Age  NaN형태  나이의 평균값으로 채우기
# 해결2] 열추가 city '서울' , '제주',  '독도', '수원' 
# 해결3] Age필드명을  Years 이름변경
# 해결4] city열 삭제

merge 는 같은 열이 없으면 나오지 않는다. 
concat 은 같은 열이 없어도 나온다.

'''