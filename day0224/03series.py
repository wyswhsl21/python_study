import pandas as pd
import numpy as np

sr1 = pd.Series(['고구마', '새우깡', '케익']  , index=['ㄱ','ㅅ', 'ㅋ'])
print(sr1)
print()

sr2 = pd.Series(['커피', '여름', '겨울']  )
print(sr2)
print()

sr3 = pd.Series([9800, 2400, 5600]  , ['커피', '포도', '한라'])
print(sr3)
print()

# city 딕트딕셔너리구조를  시리즈화 
city = {'Cal':3928483, 'Tex': 389234234, 'NY': 3829392384, 'CK': 23113214, 'LA': 9219384}
pop = pd.Series(city)
print(pop)
print()












print()
print()
