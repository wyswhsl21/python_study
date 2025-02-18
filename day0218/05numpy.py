import numpy as np


a= np.array([3,5,9])
b= np.array([2,7,4])
c = a+b
print(c)


print()



x = np.concatenate((a,b))
print(x)
x.sort()
print(x)

print()

x= np.zeros([3,5]) # 0으로 행렬 만들어주는 메소드 zeros
print(x)
print()
y= np.ones([3,5]) # 1로 행렬 만들어주는 메소드 ones
print(y)
print()


a= np.random.randint(1,6,1)
print(a)
print()