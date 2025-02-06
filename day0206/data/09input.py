# 09input.py

name, age, fit = '', 0, 0
grade = ''
# name = input('이름입력 >>>')
# age = input('나이입력 >>>')
# fit = input('피트입력 >>>')

print(name, age, fit)

# 문제해결 혜택조건 입력한 나이 + 10 , 입력한 피트 2.1
print()
# print(f'입력받은 이름 ={name}')
print(f'입력받은 나이={int(age)}')
# print(f'입력받은 피트={float(fit) *2.1}')

if int(age) >= 65:
    grade = '노년'
elif int(age) > 30:
    grade = '장년'
elif int(age) > 20:
    grade = '청년'
elif int(age) > 14:
    grade = '청소년'
else:
    grade = '초등'

print(grade)
# 나이조건
# 청소년에 영유아 17세미만
# 18 ~30 청년
# 31 ~ 65세 장년
# 65세 이상 노년
# file

f = open('C:/Mtest/새파일.txt', 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# readline 함수 이용하기 단순 파일 읽는 함수수

f = open("C:/Mtest/새파일.txt", 'r')
while True:

    line = f.readline()
    if not line: break
    print(line)
f.close()

# readlines 함수 파일을 읽고 리스트로 출력 받는 함수

f = open('C:/Mtest/새파일.txt', 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(f'파일의 행 {line}', end=' ')
f.close()

# read 함수 파일을 읽고 문자열로 리턴

f = open('C:/Mtest/새파일.txt', 'r')
data = f.read()
print('data 는 ', data)
f.close

# read 함수 사용해서 새로운 내용 추가하기

f = open("C:/Mtest/새파일.txt", 'a')
for i in range(11, 20):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()

# with 문을 사용하면
# 파일을 열면 (open) 항상 닫아주어야 하기 때문에
# 자동으로 처리할 수 있는 방법이 with이다

with open('foo.txt', 'w') as f:
    f.write('Life is too short, you need python')
