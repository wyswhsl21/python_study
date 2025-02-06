# 08ifpass.py

kor, eng, total = 100, 30, 0
avg = 0.0
result = '안내문'

total = kor + eng
avg = float(total) / 2

if (avg >= 70) or (kor >= 60) or (eng >= 60):
    result = '축합격'
else:
    result = '재시험'

print(f'총점 = {total}')
print(f'평균 = {int(avg)}')
print(f'{result} 대상자 입니다')
print('08ifpass.py문서')

# 공지사항
# 재해 보험 가입을 위해서 2시 전까지 주민등록번호가 필요

#문제0 평균숫자를 정수형으로 표시, 반올림적용
#문제1 평균을 변수 선언해서 처리, 출력
#문제2 평균점수 70점부터 축합격 0~69 재시험
#문제3 합격조건을 평균이 70점부터 과락점수 60점부터 국어,영어
'''
두번째 if ~ else 
 if 조건 :
      조건만족시처리
 else :
      조건불만족처리
'''
print()
