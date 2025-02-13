# 람다식에 대해서

import re

# 람다 함수 사용법
add = lambda a, b: a * b
result = add(3, 4)
print('결과는', result)

mul = lambda x: 3 * x
mul(10)
print(mul(10))
'''
book 함수 매개인자 x return 값 x 
note함수에서 book() 호출
'''


def book():
    print('이 책은 히가시노 게이고 소설입니다.')


def note():
    book()


if __name__ == '__main__':
    note()

print(f'{(lambda x:5*x+2)(10)}')

print(f'{list(map(lambda x:x**2,[1,2,3,4,5]))}')
print(f'{[i**2 for i in list(range(1,6))]}')

print(f'{(lambda x,y,z:x*y*z)(4,5,6)}')
print(f'{list(map(lambda x: x*2,('1234').split()))}')
ad = list(map(lambda x: x*2,('1234')))
print(ad)