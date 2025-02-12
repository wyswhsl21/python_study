# worklotto.py
import random
lotto = [32,7,12,45,25,39]



print(' -' * 30)
lotto.sort()

#첫번째 로또 소트 오름차순


#총 6회 발생 내코드
result =[]
result.clear()
while len(result) < 6:  
    com =(random.randint(1,45))
    if com not in result:
        result.append(com)
    
result.sort()
for j in result:
    print(f' {j}', end= " ")

# 선생님 코드 집합으로 만들어서 중복 못하게 변경
lotto = set()
flag = True
while flag :
    lotto_data = random.randint(1,45)
    if len(lotto) >= 6:
        flag = False
    else:
        lotto.add(lotto_data)
print()

lotto2 = list(lotto)
lotto2.sort()

print(lotto2)

'''
로또 첫번째 방법

'''

class luckyLotto:
    result = list()
    def random_data():
        return random.randint(1,45)
    def is_in_number(num):
        if num not in result:
           return result.append(num)
        else:
            return print('로또에 이미 중복된 값이 있습니다.')
    def output_lotto_number(result):
         for i in result:
             print(f'{i}',end=' ')


a= luckyLotto()


