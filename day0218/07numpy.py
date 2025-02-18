import numpy as np
import pandas as pd


lotto = [27,9,31,45,2,16]
data = ['국어','영어','수학','체육']
flag =[True,False,True]

sr1 = pd.Series(lotto)
sr2 = pd.Series(data)
sr3 = pd.Series(flag)

print(type(sr1))
print(type(sr2))
print(type(sr3))
print()

print(sr1)
print(sr2)
print(sr3)