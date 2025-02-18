import numpy as np



a= np.random.randint(1,46,1) #1개 갯수
print(a)
print()


b= np.random.uniform(1,46,6) #1개 갯수
print(b)
print()


c= np.random.rand(1,46,6) # 6개 발생인데 실수형
print(c)
print()

# 15개 데이터 4행 * 3열 에러발생
d= np.random.rand(12).reshape(4,3) #실수형태 1행 15열 원래  reshape(행,열)
print(d)
print()