import numpy as np #필수 임포트 

# my = np.array( ( [1,2,3,4], [5,6,7,8] , [9,2,5,7] ) ) 정답
# my = np.array( [ [1,2,3,4], [5,6,7,8] , [9,2,5,7] ] ) 정답

score = np.array(  [ [1,2,3], [4,5,6], [7,8,9], [10,11,12] ]    ) 
print(score)
np.save('./data/myarray.npyLee',score)
print(f'./data/myarray.npykim 파일 저장 성공')
print()

import time
time.sleep(1)
print(np.load('./data/myarray.npyLee.npy'))
print('/data/myarray.npyLee 파일 열기 성공')


















print()
print()