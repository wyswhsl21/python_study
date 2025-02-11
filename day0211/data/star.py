cnt = 0

for i in range(1, 6):
    print('*' * i, )

for row in range(6):
    for col in range(0, row, 1):
        print('❤️', end=' ')
    print()
