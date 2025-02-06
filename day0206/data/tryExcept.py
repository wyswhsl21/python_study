# try except 문
# except 는 try catch 문 같은건가 ..? error 를 잡아주네!
num1, num2, total, mok = 0, 0, 0, 0

# 연산처리 더하기,몫 연산후 출력

try:
    num1 = int(input('num1 입력>>> '))
    num2 = int(input('num2 입력>>> '))
    total = int(num1) + int(num2)
    mok = int(num1) / int(num2)

except Exception as e:
    print(f'오류 발생했습니다. 오류는 {e}')
