import pandas as pd
import numpy as np

# city 딕트딕셔너리구조를  시리즈화 
city = {'Cal':3928483, 'Tex': 389234234, 'NY': 3829392384, 'CK': 23113214, 'LA': 9219384}
pop = pd.Series(city)
print(pop)
print()

print(pop.values)  #리스트형태로 출력
print()
print(pop.index)
print()

#해결2] Tex ~ CK 추출
print(pop['Tex':'CK'])

#해결3] NY 추출
print(pop.ny)
print(pop['ny'])
print()


#해결3] 정답 NY 추출
print(pop.NY)
print(pop['NY'])
print()

'''
해결1] index추출,  values추출  
해결2] Tex ~ CK 추출
해결3] NY 추출

Cal       3928483
Tex     389234234
NY     3829392384
CK       23113214
LA        9219384
dtype: int64
'''









print()
print()
