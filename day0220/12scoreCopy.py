#2월 19일 목요일 숙제내용 score.csv 파일 kor ~ dept , hap, avg
#성별 gen 맨 마지막 열에 삽입 추가 
#남자 True , 여자 False 
#성별 조회 남자 True
#score_gender.csv 파일 저장 
# 숙제항목 x no사번 hap 열 / avg 열 차트 그리는 연습 bar,scatter 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
from matplotlib import font_manager
from matplotlib.collections import EventCollection
import time

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

path ='./data/score.csv' 
df = pd.read_csv(path,encoding='euc-kr')
# print(df)
time.sleep(1)

print(df.head()) #상위 5건 노출
print()
print(df.tail()) #하위 5건 노출 
print()
time.sleep(1)
print(df.head(10)) #상위 10건 노출
print()

print(df.describe()) #각 값들 출력
print()
print(df.info()) #non null 값이 존재하는지 확인
print()




print()
print(df)
print(df['no'], ' ', df['hap']) 
x = df['no']
y = df['hap']
plt.bar(x, y, color='green')
plt.show()
print('그래프 출력 확인 ok ')



# kor = df.kor 
# eng = df.eng
# mat = df.mat
# total = kor+eng+mat
# avg  = round(total/3, 2)
# df.insert(5,['hap'],total,True)
# df.insert(6,['avg'],avg,True)
# df['gen']=[True,True,True,True,True,True,False,False,False,False,False,False,False,False,False]
# selectedManData = df[df['gen'] != True].index
# dfCopy = df
# dfCopy.drop(selectedManData,inplace=True)
# score_gender = pd.DataFrame(dfCopy)
# score_gender.to_csv('./data/score_gender.csv',index=False)
# print('./data/score_gender.csv 저장 완료 하였습니다.')



