import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
from matplotlib import font_manager

font_name = font_manager.FontProperties(
    fname='c:/windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

path = './data/score.csv'

df = pd.read_csv(path, encoding='euc-kr')
kor = df.kor
eng = df.eng
mat = df.mat

tot = kor + eng + mat
avg = round(tot / 3, 2)
df.insert(5, ['tot'], tot, True)
df.insert(6, ['avg'], avg, True)

passList = []

for k, v in enumerate(df['avg']):
    if v >= 60:
        passList.append('O')
    else:
        passList.append('X')

df.loc[df.avg >= df.avg.mean(), 'pass'] = 'O'
df.loc[df.avg < df.avg.mean(), 'pass'] = 'X'
print(df)
print()
df.insert(7, ['pass'], passList, True)
dfCopy = df
score_pass = pd.DataFrame(dfCopy)
print(dfCopy)
'''
tot컬럼필드  새로추가   tot = kor + mat + eng
avg컬럼필드  새로추가   avg = tot/3 
pass컬럼열   새로추가   60점부터 축합격대신 O, 60점미만 0~59 X
최종의 결과
        kor  mat   eng   tot    avg     pass
고길동   40    70   80   190    63.33    O
김희동   55    55   95   205    68.33    O
김연아   66    66  100   232    77.33    O
손흥민   77    20   77   174    58.00    X
박찬호   34    40   90   164    54.67    X
'''
