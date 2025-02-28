# import matplotlib
# import matplotlib.pyplot as plt        # 첫번째
# from  matplotlib import pyplot as plt  # 두번째
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

# 음수표기 관리
import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import pandas as pd
import numpy as np
import seaborn as sns 
import time


#----------------------------------------------------------------------------------------------------------
from sklearn.preprocessing import OneHotEncoder

data =['cat','dog','여름','mouse']
# 해결 1] OneHotEncoder 처리는 판다스의 DataFrame 화 ({'Animal':[]})
# OneHotEncoder 처리 - 넘피접근 , 판다스 접근
# 넘피 접근 = np.array() 판다스 접근할때 DataFrame()
df = pd.DataFrame({'Animal':data})

print(df,'데이터 프레임')






#해결 2] one_hot_encoder =OneHotEncoder()
one_hot_encoder =pd.get_dummies(df,columns=['Animal'])
print('OneHotEncoder 전',data)
print('OneHotEncoder 후',one_hot_encoder)
decoder = one_hot_encoder.rename(columns=lambda x: x.replace('Animal_', ''))
print(decoder,'decoder 1111111111111')
ret_decoder = pd.from_dummies(decoder)
print(ret_decoder , 'decode 222222222')

print('OneHotEncoder 테스트중 ')
# result = one_hot_encoder.fit_transform(df)
# print(result,'reuslt')

# 해결 3] True/False 불값 대신 원래 데이터 전환
restore_df = pd.from_dummies(one_hot_encoder)
print('레이블 원래', restore_df)
df_restored = restore_df.applymap(lambda x: x.replace('Animal_', '') if isinstance(x, str) else x)
print(df_restored)

#해결 4] idmax를 이용한 방식

# 나의 방식 applymap 이용해서 데이터 순회 후 값 바꿔주기
restore_df = pd.from_dummies(one_hot_encoder)
print('레이블 원래', restore_df)
df_restored = restore_df.applymap(lambda x: x.replace('Animal_', '') if isinstance(x, str) else x)
print(df_restored)


# decoder2 = one_hot_encoder.idxmax(axis=1).str.replace('Animal_','') idxmax 는 열 기준으로 1이 있는지 찾아서 1이 있는 데이터의 컬럼명을 Animal_ 삭제 하는것!
decoder = pd.from_dummies(one_hot_encoder)
decoder = decoder.rename(columns=lambda x: x.replace('Animal_', ''))
# decoder = decoder.replace(to_replace=r'Animal_', value='', regex=True)
print(decoder,'decoder')
'''
레이블 전 ['cat', 'dog', 'mouse', '여름@#&']
레이블 후 [0 1 2 3]
문자화 후 ['cat' 'dog' 'mouse' '여름@#&']

'''
