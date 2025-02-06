# 06if.py

kor, eng, total = 40, 100, 0
grade = ''
avg = 0.0
result = ''

total = kor + eng
avg = round(total / 2)

if 90 <= avg and 100 >= avg:
    grade = 'A'
elif 80 <= avg and 89 >= avg:
    grade = 'B'
elif 70 <= avg and 79 >= avg:
    grade = 'C'
elif 60 <= avg and 69 >= avg:
    grade = 'D'
else:
    grade = 'F'

print('-' * 50)

print(f'결과점수 = {total}')
print(f'평균점수 = {(avg)}')
# 평균 점수를 100점에서 90 점 A , 89~80 B 79~70 C 69~60 D 59~ 0 F
# 선수 변언 후 초기화
print(f'당신의 학점은 {grade}')
print('-' * 50)
'''
세번쨰 if ~ elif ~ else



'''
