
'''
순서1] spam_data.csv파일 열기

순서2] 사용자정의함수 clear_text   clear_spam  
 ㄴ 사용자정의함수 사용 구현 안해도 상관없습니다  
 ㄴ 정규식추천  대환영 
 ㄴ 한글문자만 추출 - 숫자,특수문자, 영문자의 대소문자제외시키고 한글만 추출 

순서3] list comprehension이용대신 for반복문안에서 if~else spam 0, ham 1  
순서4] list comprehension이용해서 spam 0일때 "고려", ham 1일때 "안심"
응용안해도 됩니다 시리즈, 데이터Frame  
실습시간  10분 할애 17분까지 처리 

시각화적용안함
판다스의 시리즈, 데이터Frame  사용하고 싶어요. 각자 처리절차 맞추어서 선택 
출력결과는 리스트나 문자열 추출 가능 

우리나라 대한민국 우리나라 만세 보이스피싱 정다정 최고 나는 대한민국 사람 보험료 원에 평생 보장 마감 임박 나는 홍길동 성산포 바다 파도소리 높은하늘
['우리나라 대한민국 우리나라 만세', '보이스피싱 정다정 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동', ' 성산포 바다 파도소리 높은하늘', '']

'''

import pandas as pd
import numpy as np
import re

fname = './data/spam_data.csv'
spam_data = pd.read_csv(fname, encoding='cp949', header=None )  #read_csv함수(1,2인코딩, 3제목헤더 제목없을때 )
print(spam_data) 

target = spam_data[0]
texts = spam_data[1]

print( target )
print()
print( texts )
print()

print( type(target), ' ' , type(texts) ) #<class 'pandas.core.series.Series'>   <class 'pandas.core.series.Series'>
print()

def clear_text(data):
    msg = re.sub('[!@#$%^&*()]|[0-9]','', data )  
    msg = re.sub('[,.?!:;\'\"]','', msg)
    msg = re.sub('[a-zA-z]','', msg)
    print(msg)
    print()
    print(' '.join(msg.split()))


clear_text(target)

target = spam_data[0]
print(str(texts))
print()


info  =  [ 1  if t=='spam' else 0  for t in target ]
print(info)
print()

info  =  [ '대기'  if t=='spam' else  '안심'  for t in target ]
print(info)
print()


# 시리즈, DataFrame, re정규식,  파일처리 



'''
message = ['spam', 'ham', 'spam', 'ham', 'spam']

dummy = []
for i in message :
    if i == 'spam' :
        tmp = 1
        dummy.append(tmp)
    elif i == 'ham' :
        tmp = 0
        dummy.append(tmp)
print(dummy)  # [1, 0, 1, 0, 1]


# print('list comprehension')
# print( [1 if k=='spam' else 0 for k in message]) #[1, 0, 1, 0, 1]
'''