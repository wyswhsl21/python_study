import pandas as pd


path ='./data/score.csv'

score = pd.read_csv(path,encoding='euc-kr') # csv 파일을 읽어오는거 

print(score)
print()

# print(score.loc[4:10])
# print(score.loc[:,'kor':'mat']) #loc

# 해결 5행 10행 추출
# 모든행 kor,eng,mat 3개 필드열 추출


#해결3] kor 필드열 최대값 추출 max 이용
# print(score['kor'].max())

# # 최댓값을 가진 행 찾기
# max_row = score.loc[score['kor'].idxmax()]
# print(max_row)

# max_index = score['kor'].idxmax() # 최댓값을 가진 행의 인덱스
# max_value = score.loc[max_index,'kor'] #해당 인덱스에서 kor 열의 값

# print(f'최댓값 : {max_value}, 인덱스: {max_index}')

#해결4] kor필드 , eng필드 ,mat필드 접근할때 score 명명 최대값 

# mat필드  접근해서 total합계, avg평균
kor = score.kor 
eng = score['eng']
mat = score.mat
total = kor+eng+mat
avg  = round(total/3, 2)
score.insert(5, ['hap'], total,True)
score.insert(6, ['avg'], avg,True)
print(score)
#해결 4 모든행 hap,avg 
# total = score.loc[:,'kor':'mat'].sum().sum()
# mean = score.loc[:,'kor':'mat'].mean().mean()
# # score.insert(위치,열이름,True)
# score.insert(5,['hap'],total,True)
# score.insert(6,['avg'],mean,True)


print(score)



selected_columns2 = score[['no','kor', 'eng']] #리스트로 바로 특정 열 선택
selected_columns = score.iloc[:,[0,-1,-2]] # 특정 열 이용
selected_columns1 = score.loc[:,['no','avg','hap']] # loc 이용한 열 선택
print(selected_columns)
print(selected_columns1)
print(selected_columns2)