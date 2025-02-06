# 구구단
dan, n = 7, 1

# 첫번째
print(f'{dan} * {n} = {dan * n}')
print(f'{dan} * {2*n} = {dan * 2*n}')
print(f'{dan} * {3 *n} = {dan * 3*n}')

# 두번쨰
for x in range(dan, dan + 1, 1):
    for y in range(1, 10, 1):
        print(f'{x} * {y} = {x * y}')

# 세번쨰
cnt = 1
while cnt < 10:
    print(f'{dan} * {cnt} = {dan * cnt}')
    cnt += 1

# for /while 사용 안함
#  for
#  while
