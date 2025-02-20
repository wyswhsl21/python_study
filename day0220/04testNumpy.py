import math
import numpy as np
import time as time



# 해결 1~5   숫자 발생 타입 실수 30갯수 

x= np.linspace(1,5,30) #시작 ,끝 ,갯수 갯수를 빼면 default ==50개 
print(x)


a = np.array( [9,5,4,3,1,2,3,4,3,2,4,1,2,3,7,3,1,2,1,2,5,1,7,1,2,2,1,3] )
ret = np.unique(a)  #[1 2 3 4 5 7 9]
print(ret)
print()

print('trim적용')
b = np.array( [0,0,0,3,0,2,3,4,0,2,4,1,2,3,7,3,1,2,0,0,5,1,7,1,0,0,0,0] )
print(np.trim_zeros(b))  #앞뒤 제로소거 
print(np.trim_zeros(b,trim='f'))  #앞 제로소거 
print(np.trim_zeros(b,trim='b'))  #뒤 제로소거 
print()


print(2345000)
print(f'{2345000}')
print('%d'%(234500))
print('{0}'.format(2345000))
print('{0}'.format(2345000))