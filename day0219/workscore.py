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

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

path ='./data/score.csv' 
df = pd.read_csv(path,encoding='euc-kr')
kor = df.kor 
eng = df.eng
mat = df.mat
total = kor+eng+mat
avg  = round(total/3, 2)
df.insert(5,['hap'],total,True)
df.insert(6,['avg'],avg,True)
df['gen']=[True,True,True,True,True,True,False,False,False,False,False,False,False,False,False]
selectedManData = df[df['gen'] != True].index
dfCopy = df
dfCopy.drop(selectedManData,inplace=True)
score_gender = pd.DataFrame(dfCopy)
score_gender.to_csv('./data/score_gender.csv',index=False)
print('./data/score_gender.csv 저장 완료 하였습니다.')



# 📌 1. CSV 파일 불러오기
file_path = './data/score_gender.csv'
genderDf = pd.read_csv(file_path)

# 📌 2. 'no' 컬럼을 기준으로 'hap'(총합)과 'avg'(평균) 가져오기
total_scores = genderDf.groupby("no")["hap"].sum()  # 사번별 총합
mean_scores = genderDf.groupby("no")["avg"].mean()  # 사번별 평균

# 📌 3. NumPy 배열 변환 & 정렬
xdata1 = total_scores.values
xdata2 = mean_scores.values

xdata1_sorted = np.sort(xdata1)
xdata2_sorted = np.sort(xdata2)

# ✅ NaN 값 방지 (0 이하 값 변환)
ydata1 = np.sqrt(np.maximum(xdata1_sorted, 0))
ydata2 = np.log1p(np.maximum(xdata2_sorted, 0))

# 📌 4. 그래프 그리기
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# ✅ (1) 바 차트: 사번별 hap 값 (총합)
axs[0,0].bar(total_scores.index, total_scores.values, color='tab:blue')
axs[0,0].set_title("사번별 총합 (hap)")
axs[0,0].set_xlabel("사번 (no)")
axs[0,0].set_ylabel("hap 총합")

# ✅ (2) 산점도: 사번별 avg 값 (평균)
axs[0,1].scatter(mean_scores.index, mean_scores.values, color='tab:orange')
axs[0,1].set_title("사번별 평균 (avg)")
axs[0,1].set_xlabel("사번 (no)")
axs[0,1].set_ylabel("avg 평균")

# ✅ (3) 선 그래프: 총합 변환값 (ydata1)
axs[1,0].plot(xdata1_sorted, ydata1, color='tab:blue')
axs[1,0].set_title("변환된 hap 데이터 (sqrt)")
axs[1,0].set_xlabel("hap 값")
axs[1,0].set_ylabel("sqrt(hap)")

# ✅ (4) 선 그래프: 평균 변환값 (ydata2)
axs[1,1].plot(xdata2_sorted, ydata2, color='tab:orange')
axs[1,1].set_title("변환된 avg 데이터 (log1p)")
axs[1,1].set_xlabel("avg 값")
axs[1,1].set_ylabel("log1p(avg)")

# ✅ 레이아웃 자동 조정
plt.tight_layout()

# 📌 5. 그래프 출력
plt.show()