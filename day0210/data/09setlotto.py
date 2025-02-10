# 09setlotto.py

import random

print('lotto 난수 6개 생성 복합 set 응용')
lotto =set()

flag =True

while flag :
    lotto_data = random.randint(1,45)
    if lotto_data in lotto:
        continue
    else:
        lotto.add(lotto_data)
        print(f'로또 숫자가 출력 되었습니다. \n숫자는 ={lotto_data}')
    pass
    if len(lotto) >=6:
        break
lotto_list = sorted(lotto)
print(f'로또 번호 추출 : {','.join(map(str,lotto_list))}')


# 문제 로또 발생 후 오름차순 소트해서 출력
