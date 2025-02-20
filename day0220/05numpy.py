import numpy as np
my = np.array( [
    [ [1,2,3,4], [56,43,7,8] ],
    [ [9,2,3,7], [39,43,5,9] ],
    [ [1,5,3,8], [24,43,6,1] ],
    [ [6,2,3,4], [71,43,2,3] ],
    [ [3,1,7,6], [62,51,7,9] ],
 ])


print(my)

print('my.size = ' ,my.size )
print('my.shape = ' , my.shape ) # 행렬의 구조 (행,     ,열)
print('my.ndim = ', my.ndim)  #몇차원 행렬인지 ?
# print('my.len = ', len(my)) 