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
result = label_encoder.fit_transform(data)
print(result)








print()
print()
