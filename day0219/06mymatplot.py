import matplotlib.pyplot as plt
#음수표기 관련
import matplotlib
from matplotlib import font_manager
import matplotlib as mpl
import numpy as np

font1 = {'family': 'serif',
         'color': 'b',
         'weight': 'bold',
         'size': 14
         }

font2 = {'family': 'fantasy',
         'color': 'deeppink',
         'weight': 'normal',
         'size': 'xx-large'
         }


year =[1995,2000,2005,2010,2015,2020,2025]
gdp =[300.2,543.3,1075,2876.5,5989.3,10283.4,14504.5]

plt.plot(year,gdp,color='red',marker='o',linestyle='solid')
plt.title('한국 GDP 실상')
plt.xlabel('year',fontdict=font1,loc='right')
plt.ylabel('gdp',fontdict=font2,loc='top')
plt.show()
#labelpad 여백 지정
#fontdict 파라미터로 폰트 스타일 지정 가능
#위치 지정하기 loc 속성 이용

#음수표기 관리

mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

#한글 
font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)