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
#--------------------------------------------------------------------------------------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import r2_score

data = {  'x':[13, 19, 16, 14, 15, 14] , 
          'y':[40, 83, 62, 48, 58, 43] }

df = pd.DataFrame(data)
lr = LinearRegression() 
x = df['x'].values[ :,  np.newaxis] 
lr.fit(x, df['y'])

y_pred = lr.predict(x)
y =  [40, 83, 62, 48, 58, 43]
print('mae결과 =', mean_absolute_error(y,y_pred))   # 1.625 
print('mse결과 =', mean_squared_error(y,y_pred))      # 5.172749391727503 
print('rmse결과 =', root_mean_squared_error(y,y_pred))  # 2.2743679103714736 
print('mape결과 =',  mean_absolute_percentage_error(y,y_pred)) #0.03225264741536682
print('r2_score결과 =', r2_score(y,y_pred))   # r2_score결과 = 0.9753156179610034                                 



















print()
print()
