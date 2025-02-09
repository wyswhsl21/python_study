# 11lotto.py
import random
lotto = [32,7,12,45,25,39]
print(lotto)


print(' -' * 30)
lotto.sort()
print('오름차순',lotto)
#첫번째 로또 소트 오름차순


#총 6회 발생 
com = random.randint(1,45)
print(f'난수 = {com}')


