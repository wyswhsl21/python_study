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

import sklearn
data =[
    [1,2,3,np.nan,5],
    [np.nan,7,8,9,10],
    [11,12,np.nan,14,15]
    ]


data = np.array(data)
df = pd.DataFrame(data)
df.fillna(df.median(),inplace=True)
print(df)
print('결측치 처리전 \n',data)
print()


#해결 1] 결측값 대체 어떤값으로 평균, 중위값, 본인마음대로
'''
데이터 유형	추천 채우기 방법
연속형 데이터	평균(mean), 중앙값(median), 선형 보간(interpolation)
범주형 데이터	최빈값(mode), 랜덤 샘플(random choice)
시계열 데이터	이전 값(ffill), 다음 값(bfill), 선형 보간(interpolation)
이상치가 있는 경우	중앙값(median), 랜덤 샘플링(random choice)
복잡한 데이터	머신러닝 모델(SimpleImputer, KNNImputer)
'''








print()
print()
