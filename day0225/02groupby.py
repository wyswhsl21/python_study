import pandas as pd
import numpy as np

data_dict	=	{
				'Name':	['aaa',	'bbb',	'ccc',	'ddd',	'eee',	'fff' ,	'eee'],
				'City':	['시카고',	'뉴욕',	'샌프란시스코',	'시카고',	'로스앤젤레스',	'시카고',	'뉴욕'],
				'Years':	[2001,	2023,	1995,	1985,	1987,	1994,	1989]
}





df	= pd.DataFrame(data_dict) # data 객체 , index 넣어줄 수 있음.
group_city = df.groupby('City')['Years'].mean()
gpYears = df.groupby('Years') #숫자
print(df)
max_years = df['Years'].max()
min_years = df['Years'].min()
mean_years = df['Years'].mean()


print(df)
print(f'max Years = {max_years}, min Years = {min_years} , mean_years ={mean_years} group_city = {group_city} ')
print()

'''
해결1] Years 컬럼 평균 최소 , 최댓값
해결2] 그룹화 Years 의 평균
해결3] 그룹화 City의 평균 문자의 평균




'''