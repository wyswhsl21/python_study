# 05 testtuple.py

mytuple = ('제주', 37.75148, 126.34136, '시청', 36.73982, 127.92851)
print(mytuple)

# enumerate

for i, e in enumerate(mytuple):
    print(i, ':', e)

for value in range(len(mytuple)):
    print(mytuple[value], end=' ')

# 문제 data 리스트를 for 반복문으로 출력
datas = ['제주', 34.56756, '시청', 36.73982]
for data in datas:
    print(data, end=" ")
