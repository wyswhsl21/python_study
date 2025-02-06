# 10inputexcept.py
num1, num2, total, mok = 0, 0, 0, 0
num1 = int(input('num1 입력>>> '))
num2 = int(input('num2 입력>>> '))
# 연산처리 더하기,몫 연산후 출력

total = int(num1) + int(num2)
mok = int(num1) / int(num2)

print(
    f'{num1} + {num2} 합 = {total} \n{num1} / {num2} 몫은 = {round(mok,2)} 입니다.')
print()

print()
