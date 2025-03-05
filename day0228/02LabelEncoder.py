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
from sklearn.preprocessing import LabelEncoder

data =['cat','dog','mouse']
# 해결 1] LabelEncoder는 문자데이터 속도를 위해서 숫자화

label_encoder=LabelEncoder()

result = label_encoder.fit_transform(data) # encoder 레이블 하는 함수 
print('레이블 전',data)
print('레이블 후',result)



#해결 2] 레이블 인코더 된것 숫자를 다시 문자화 LabelDecoder화
decoder = label_encoder.inverse_transform(result) # decode 는 inverse_transform 으로 한다.
print('문자화 후',decoder)


'''
레이블 전 ['cat', 'dog', 'mouse', '여름@#&']
레이블 후 [0 1 2 3]
문자화 후 ['cat' 'dog' 'mouse' '여름@#&']
레이블을 하면 문자가 숫자로 바뀜. 데이터 정렬 기준은 알파벳 순인거 같음.
'''





print()
print()
