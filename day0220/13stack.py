import math
import numpy as np
import time as time
 


#에러  a = np.array(  [1,2], [3,4]  ) # Field elements must be 2- or 3-tuples, got '3'
a = np.array( [ [1,2], [3,4] ] )  # [ ] 리스트
b = np.array( ( [5,6], [7,8] ) )  # ( ) 튜플 
print()
print(a) # [[1 2]  [3 4]]
print()
print(b) # [[5 6]  [7 8]]
print()
# print(np.transpose(a))

print(np.vstack([a,b]))
print()
print(np.hstack([a,b]))

# vstack 은 열을 기준으로 쪼개서 쌓는거고 
# hstack 은 행을 기준으로 1,2,5,6 3,4,7,8