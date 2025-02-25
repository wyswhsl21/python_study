import pandas as pd
import numpy as np

df1 = pd.DataFrame( {
    'ID' : [1111, 2222, 3333] ,
    'Name' :  ['고희동', '홍길동', '봄여름']
} )
print(df1)
print()

df2 = pd.DataFrame( {
    'ID' : [1111, 2222, 3333] ,
    'City' :  ['서울', '제주도', '수원']
} )
print(df2)
print()

print('\n간단한 merge 테스트')
df_merge = pd.merge(df1, df2, on='ID') #기본값  on='ID' 생략가능
print(df_merge)
print()

print('\n간단한 concat 테스트')
#df_concat = pd.concat( [df1, df2], axis=0)   # axis=0 기본
df_concat = pd.concat( [df1, df2], axis=1 )   # axis=1
print(df_concat)
print()
'''
간단한 concat 테스트  axis=0 
     ID Name City
0  1111  고희동  NaN
1  2222  홍길동  NaN
2  3333  봄여름  NaN
0  1111  NaN   서울
1  2222  NaN  제주도
2  3333  NaN   수원
'''

'''
merge(1,2,3,4,5,6,7,8,9,10,11,12) , concat(), join()  판다스 연결

fillna(), rename(), drop()
해결1] 나이 Age  NaN형태  나이의 평균값으로 채우기
해결2] 열추가 city '서울' , '제주',  '독도', '수원' 
해결3] Age필드명을  Years 이름변경
해결4] city열 삭제
int()  round()  str() type()  astype()  
mean() max() min() median()
'''












print()
print()