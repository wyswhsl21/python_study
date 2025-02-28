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

from sklearn.preprocessing import OneHotEncoder
# 해결5] 넘피 이용 OneHotEncoder함수 사용
data =['cat','dog','여름','mouse']
numpy_data = np.array(data).reshape(-1, 1)
one_hot_encoder5 = OneHotEncoder()
result = one_hot_encoder5.fit_transform(numpy_data) #에러발생
restore_numpy_data = one_hot_encoder5.inverse_transform(result).flatten()
print('numpy_one hot 인코딩 전 \n ',numpy_data.flatten(),)
print('numpy_one hot 인코딩 후 \n ',result,)
print('numpy decode 후 \n', restore_numpy_data)


print('#------------------------------------------------------------------------')
#----------------------------------------------------------------------------------------------------------
from sklearn.preprocessing import OneHotEncoder

data =['cat','dog','여름','mouse']
# 해결 1] OneHotEncoder 처리는 판다스의 DataFrame 화 ({'Animal':[]})
# OneHotEncoder 처리 - 넘피접근 , 판다스 접근
# 넘피 접근 = np.array() 판다스 접근할때 DataFrame()

# print(df,'데이터 프레임')






'''
레이블 전 ['cat', 'dog', 'mouse', '여름@#&']
레이블 후 [0 1 2 3]
문자화 후 ['cat' 'dog' 'mouse' '여름@#&']

'''
