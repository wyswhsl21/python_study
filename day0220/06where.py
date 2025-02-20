import numpy as np



#1 ~ 4 초급 5~7 중급 8~10 고급
eng = np.array([7,5,3,9,1,2,4,6])
print(np.where(eng >=5,1,0))

print(f'{np.where(eng > 4,np.where(eng >= 8 ,'고급','중급'),'초급')}')

# 넘피에서 조건절 where 구문

data = np.arange(1,11)
print(data)

print(np.where(data < 5,data,5*data))

