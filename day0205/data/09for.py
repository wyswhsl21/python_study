# 09for.py

print('처음 for 반복문 연습')

for i in range(0, 10, 2):
    print(i, end=" ")
print()
for y in range(1, 11, 1):
    print(y, end=" ")
print()
# 리스트 크기를 미리 확보
a = [0] * 20

# 초기값 설정
a[0] = 0
a[1] = 1

# 피보나치 수열 계산
for x in range(2, 20):
    a[x] = a[x - 2] + a[x - 1]
    print(a[x], end=" ")  # x 값 출력

print()
print('- ' * 45)
su_ai_robot, total = 0, 0
for k in range(11):
    if k == 5: continue
    total += k
    print(f"{k} 합계 = {total}")

print('- ' * 45)
