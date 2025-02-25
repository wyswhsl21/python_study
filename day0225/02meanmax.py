import pandas as pd
import numpy as np


data_dict = { 
    'Name':	['aaa',	'bbb',	'ccc',	'ddd',	'eee',	'fff' ,	'eee'] ,
    'City':	['수원', '뉴욕', '수원', '서울', '수원', '인천', '뉴욕'] ,
    'Years': [2001,	 2023,	 1995,	1990,	1985,	2023,	2001 ]
}
df = pd.DataFrame(data_dict)
print(df)

print()
print('년도평균 ', round(df['Years'].mean(),2))   #
print('년도최소 ', round(df['Years'].min(),2))    #
print('년도최대 ', round(df['Years'].max(),2))    #
print('년도중앙 ', round(df['Years'].median(),2)) #
print()



'''
해결1] Years컬럼  평균, 최소, 최대값 

fillna(), rename(), drop()
해결1] 나이 Age  NaN형태  나이의 평균값으로 채우기
해결2] 열추가 city '서울' , '제주',  '독도', '수원' 
해결3] Age필드명을  Years 이름변경
해결4] city열 삭제
int()  round()  str() type()  astype()  
'''



















print()
print()