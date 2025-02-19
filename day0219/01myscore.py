import pandas as pd
import time
path ='./data/score.csv'

# 해결 1 판다스 이용해서 path 문자열
score = pd.read_csv(path,encoding='euc-kr')
print(score)

print()

#해결 2 hap =kor +eng + mat avg = hap //3 맨 마지막 열 추가 insert()
start = time.time()
kor = score.kor 
eng = score.eng
mat = score.mat
total = kor+eng+mat
avg  = round(total/3, 2)
score.insert(5,['hap'],total,True)
score.insert(6,['avg'],avg,True)
print(score)

#해결 3] 열추가 to_csv 실습 score_all.csv
# score_all = pd.DataFrame(score)
# score_all.to_csv('./data/score_all.csv')
# print('./data/score_all.csv 저장 성공했습니다.')
# time.sleep(0.5)

print()
#해결 4번 샘플링 추출해서 저장
# score_sample = score.sample(7)
# print(score_sample)
# score_sample = pd.DataFrame(score_sample)
# score_sample.to_csv('./data/score_sample.csv')
# time.sleep(1)


#해결 5번
selected_hap_avg_columns = score[['no','hap','avg']]
print(selected_hap_avg_columns)

#해결 7
print('특정열 iloc 로 검색하기')
print(score.iloc[:,[0,2,5]])
