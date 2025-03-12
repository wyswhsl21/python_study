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
#--------------------------------------------------------------------------------------------
df =  sns.load_dataset('tips')
print(df)  ## 처음데이터 [244 rows x 7 columns]
print(df.info()) 
print()


def remove_outliers(df,column,method='IQR',threshold=3):
    df_cleaned = df.copy() #원본 데이터 보호
    
    if method == 'IQR':

        #IQR 계산
        Q1 = df_cleaned[column].quantile(0.25)
        Q3 = df_cleaned[column].quantile(0.75)

        IQR = Q3 - Q1

        #이상치 기준 설정
        upper_limit = Q3 + 1.5 * IQR   # 46.43839435626422
        lower_limit = Q1 - 1.5 * IQR    # -2.8224999999999945
    elif method == 'STD':

        mean = np.mean(df_cleaned[column])
        std = np.std(df_cleaned[column])

        #이상치 기준 설정 
        upper_limit = mean + threshold*std   # 46.43839435626422
        lower_limit = mean - threshold*std   # -6.866509110362578
    else:
        raise ValueError("method 'IQR' 또는 'STD'만 가능합니다.")
# 이상치 제거
    df_cleaned = df_cleaned[(df_cleaned[column] >= lower_limit) & (df_cleaned[column] <= upper_limit)]
    print(f"제거된 이상치 개수: {df.shape[0] - df_cleaned.shape[0]}")
    return df_cleaned


mean = np.mean(df['total_bill'])
std = np.std(df['total_bill'])








df_cleaned = remove_outliers(df,column='total_bill',method='STD')

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
sns.boxplot(y=df['total_bill'])
plt.title('이상 치 제거 전')

plt.subplot(1,2,2)
sns.boxplot(y=df_cleaned['total_bill'])
plt.title('이상치 제거 후 ')
plt.show()




