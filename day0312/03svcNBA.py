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
import imageio
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import auc, confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
#--------------------------------------------------------------------------------------------
print('- ' * 50)
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score,roc_curve #처음적는 함수
from sklearn.preprocessing import MinMaxScaler

# ------------------------------------------------------------------------------------------------ 처음 적는 함수
#iris, 타이타닉, salaryData 종속변수 target 대상 데이터를 전부 숫자 0/1 대신 문자대체
#시각화 다양하게 해서 plt.show() 처리안하면 폴더에 저장후 ~~ .gif 확장로 동영상처럼 play

import os
#순서 1]
# gif_frames 폴더가 없다면 새로 생성하기
if not os.path.exists('gif_frames'):
    os.makedirs('gif_frames')
    print('gif_frames 폴더 생성 성공했습니다.')



#순서 2] nba_source.csv
#csv 파일을 읽어 데이터 프레임화 하기
frame =[]
df = pd.read_csv('./test/nba_source.csv')
print(df)
print()
print(df.info())

#순서 3] scatterplot plt.figure(figsize=(12,8))
#Rk Player Age Team Pos G  GS MP FG FGA FG% 3P 3PA 3P% 2P 2PA 2P% eFG% FT FTA FT% ORB DRB TRB AST STL BLK TOV PF PTS Trp-Dbl Awards


plt.figure(figsize=(12,8))
sns.scatterplot(data=df, x='Player',y='3P',hue='Pos',palette='Set2')
#x = 선수별 데이터 , y= 3점슛 성공 개수, hue= 포지션별 색상 구분
#각 인자의 의미

plt.title('NBA baseket ball original')

plt.xticks(rotation=65)
plt.savefig('gif_frames/step1.png')
print(f"sns.scatterplot(data=df, x='Player',y='3P',hue='Pos',palette='Set2') 그래프저장")
frame.append(imageio.imread('./gif_frames/step1.png'))





#순서 4] df.dropna(subset=['3P','BLK','TRB'])
dropna_trb =df.dropna(subset=['3P','BLK','TRB']) #결측치 포함하는 행 제거
#새로운 데이터프레임 dropna_trb를 생성하여 결측치가 없는 데이터를 저장
plt.figure(figsize=(12,8))

sns.scatterplot(data=dropna_trb, x='Player',y='3P',hue='Pos',palette='Set2')
plt.title('NBA baseket ball original')
# x축 간격 자동 조절
ax = plt.gca()
# ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=10))  # 최대 10개만 표시
plt.xticks(rotation=65)
plt.savefig('gif_frames/step2.png')
print(f"sns.scatterplot(data=df, x='Player',y='3P',hue='Pos',palette='Set2') 그래프저장")
frame.append(imageio.imread('./gif_frames/step2.png'))

#이상치 제거 함수
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

#이상치 제거 코드
for column in ['3P', 'BLK', 'TRB']:
    dropna_trb = remove_outliers_iqr(dropna_trb, column)

#순서 5] 이상치 제거 된 df 가지고 그래프 시각화
plt.figure(figsize=(12,8))
sns.scatterplot(data=dropna_trb, x='Player', y='3P', palette='Set3')
plt.title('NBA basketball 이상치 적용')
plt.xticks(rotation=65)
plt.savefig('gif_frames/step3.png')
frame.append(imageio.imread('./gif_frames/step3.png'))

#이상치 제거

#순서 6] 
#season 데이터 프레임 생성 후 
season = pd.DataFrame({'season':['spring','summer','fall','winter',np.nan]})
print(season)
print()
#pd.get_dummies()를 사용한 원-핫 인코딩으로 변환
#pd.get_dummies()를 사용하면 각 범주를 컬럼으로 만들어 0과 1로 표현
#NaN 값은 자동으로 무시됨.
print(pd.get_dummies(season['season'])) #LaberEncoder , map (매핑)

df_encoder = pd.get_dummies(dropna_trb,columns=['Pos'],drop_first=True)
plt.figure(figsize=(12,8))
sns.scatterplot(data=df_encoder, x='Player',y='3P',hue='Pos_Forward',palette='Set3')
plt.title('NBA basketball 이상치 적용')
plt.xticks(rotation=180)
plt.savefig('gif_frames/step4.png')
frame.append(imageio.imread('./gif_frames/step4.png'))
#순서 7] step5.png sns.boxplot()
scaler = StandardScaler()
scaler_columns = ['3P','BLK','TRB']
df_encoder[scaler_columns] = scaler.fit_transform(df_encoder[scaler_columns])
plt.figure(figsize=(12,8))
sns.boxplot(data=df_encoder[scaler_columns])
plt.title('NBA bascket ball StandardScaler 적용')
plt.savefig('gif_frames/step5.png')
frame.append(imageio.imread('./gif_frames/step5.png'))

#순서 8] gif 동영상 만들기
import cv2
main = './nba_all_step.gif'
imageio.mimsave(main,frame,fps=2)
print('./nba_all_step.gif')

video = cv2.VideoCapture('./nba_all_step.gif')


while video.isOpened():
    check,frame = video.read()
    if not check:
        print('play가 종료되었습니다.')
        break
    else:
        cv2.imshow("Video", frame)
        time.sleep(0.5)
        if cv2.waitKey(25) & 0xFF == ord('q'):  # 'q'를 누르면 종료
            break

video.release()
print('학습처리 그래프 영상 종료합니다')


'''
classification_report 반드시 ROC 커브 = Receiver Operating Characteristic " 커브로 binary classfication 모델 
ROC 커브 = Receiver Operating Characteristic 커브로 binary classification 모델 
ROC커브 = Receiver Operating Characteristic" 커브로 binary classification 모델
AUC는 "Area Under  Curve "  ROC 커브 아래 부분의 면적의 너비를 말합니다.
'''

