
import numpy as np
data  = [ 175, 177, 179, 181, 183 ]   
print('총점 ' , np.sum(data))         #총점 895
print('평균 ' , int(np.mean(data)))   #평균 895/5명 = 179
print()

result = (175-179) + (177-179) + (179-179) +(181-179) +(183-179) 
print('평균차이 ', result)
print()

# data  = [ 175, 177, 179, 181, 183 ]  
cal = ( (175-179)**2 + (177-179)**2 + (179-179)**2 + (181-179)**2 + (183-179)**2) / 5
print('분산 ' , int(cal)  )  #분산 8
print('분산 ' , int(np.var(data))  )  #분산 8

print()
print('표편 ' , round( np.std(data), 3) )  #표준편차 2.828
print('표편 ' , round( np.sqrt(8), 3) )    #표준편차 2.828
print()
