#02 for.py

cnt, total = 0, 0

for i in range(10):
    if (i == 5):
        continue

    total += i + 1
    print(i, end=' ')

print(f'합계 = {total}')

for i in range(1, 10, 2):
    print(i, end=' ')
print()
print('=' * 50)
#
# 컴프리헨션을 사용하지 않고 가져오는 방법법
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result, end=' ')
# 리스트 컴프리헨션
# a의 리스트를 * 3 배수 값으로 변환 후 짝수만 가져오기
a = [1, 2, 3, 4]
result = [i * 3 for i in a if i % 2 == 0]
print(result, end=' ')

# 구구단 컴프리헨션 구현해보기

print()
result = [x * y for x in range(2, 10) for y in range(1, 10)]
print(result, end=' ')
