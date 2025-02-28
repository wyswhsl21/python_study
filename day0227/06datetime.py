

import pandas as pd
import numpy as np
import seaborn as sns 
import time

path ='./data/남북한발전전력량.xlsx'
df = pd.read_excel(path , engine='openpyxl')
# print(df)  #[9 rows x 29 columns]
print()

data = {
    'date': ['2025-02-23', '2025-01-24', '2024-03-25', '2025-02-26', '2025-02-27'],
    'sales': [100, 150, 200, 250, 300]
}


#해결 1] 판다스의 DateFrame 화 
df = pd.DataFrame(data)
# print(df)
df_month = df['date']
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek
df['quarter'] = df['date'].dt.quarter


day_mapping = {0: '월요일', 1: '화요일', 2: '수요일', 3: '목요일', 4: '금요일', 5: '토요일', 6: '일요일'}
df['day_name_korean'] = df['date'].dt.dayofweek.map(day_mapping)
print(df)



#해결 2] 월을 추출
#해결 3] 'date' 컬럼 날짜화 pd.to_datetime()
#해결 4] 요일 추출
#              ㄴ 0 일요일 1 월요일 ~