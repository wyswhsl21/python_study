import math
import numpy as np
import time as time
 

c= np.array(([1,2,3],[7,8,9]))
print(c)

print()
# 행과열을 바꿔주는 함수 transpose()
print(np.transpose(c))
print()

print(c.T)



#에러  a = np.array(  [1,2], [3,4]  ) # Field elements must be 2- or 3-tuples, got '3'
a = np.array( [ [1,2], [3,4] ] )  # [ ] 리스트
b = np.array( ( [5,6], [7,8] ) )  # ( ) 튜플 
print(a) # [[1 2]  [3 4]]
print(b) # [[5 6]  [7 8]]
print()


