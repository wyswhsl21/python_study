# 05if.py

kor, eng, total = 90, 49, 0
avg = 0.0
result = '결과출력'

total = kor + eng
avg = round(total / 2)

if (avg >= 70):
    result = '합격했습니다'
else:
    result = '재시험 해야 합니다다'

print('-' * 50)

print(f'결과점수 = {total}')
print(f'평균점수 = {(avg)}')
# 평균 점수를 70점 부터 축 합격 재시험 69이하하
print(f'당신은 시험에 {result}')
print('-' * 50)
