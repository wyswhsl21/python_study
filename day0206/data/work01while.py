# work01while.py

#su ,data , number
# 조건  % 나머지 정수형 몫 //연산
# while 반복문 탈출 if조건 break
# su = '5942'
# data = number = 0

# print(f'숫자의 역순 = {su[::-1]}')
#

nmg = 0
mok = 0
result = []

su = 5942  # 초기 값 설정

while True:
    mok = su // 10  # 몫 계산
    nmg = su % 10  # 나머지 계산
    result.append(nmg)  # 나머지를 리스트에 저장
    su = mok  # 다음 반복을 위해 몫을 새로운 su로 설정
    if mok < 10:  # 몫이 한 자리 수가 되면 마지막 값 추가 후 종료
        result.append(mok)  # 마지막 mok 값도 저장
        break
print(''.join(map(str, result)))
