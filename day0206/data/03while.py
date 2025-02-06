# while 문 공부

cnt, total = 0, 0

while cnt < 10:
    cnt += 1
    if cnt == 5: continue
    total += cnt

    print(cnt, end=' ')
print(f'합계 = {total}')
