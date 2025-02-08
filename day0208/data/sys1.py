# sys 모듈 사용하기

import sys

args = sys.argv[1:]
for i in args:
    print(i)

print('실행하나 ??')

# sys2.py

for i in args:
    print(i.upper(), end=' ')
'''
파이썬에서는 sys 모듈을 사용하여 프로그램에 인수를 전달할 수 있다.
sys모듈을 사용하려면 다음 예의 import sys 처럼 import 명령어를 사용해야 한다,

'''
