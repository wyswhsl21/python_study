# work03umin.py
jumin = '950714-2135318'
year = '2025'
myage = 0
gender = ''
jumin_last_first = int(jumin.split('-')[1][0])
juminFirstNum = jumin.split('-')[0]
calNum = int(juminFirstNum[:2])

if len(jumin) != 14: print('올바른 주민번호가 아닙니다.')

# 주민번호가 3,4 라면 2000년생생
if jumin_last_first in (3, 4):
    myage = int(year) - (2000 + calNum)
    if (jumin_last_first == 3):
        gender = '남성'
    else:
        gender = '여성'
# 주민번호가 1,2 라면 1900 년생생
elif jumin_last_first in (1, 2):
    myage = int(year) - (1900 + calNum)
    if (jumin_last_first == 1):
        gender = '남성'
    else:
        gender = '여성'
    # 그 외 경우 올바른 주민번호 아님.
else:
    print('올바른 주민 번호가 아닙니다.')

print()
print(f'나의 나이는 {myage}')
print(f'내 성별은 {gender}')
print()
'''
문제 1 나이계산
문제 2 성별 추출출
변수이름 여러분 마음대로


선택옵션 주번 길이 체크 ,성별 1/2 , 3/4 
'''
