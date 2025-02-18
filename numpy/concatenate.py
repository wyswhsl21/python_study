import numpy as np



# array 병합과 분리
x= np.array([[1,1],[2,2]])
y= np.array([[5,6],[3,4]])

z= np.concatenate((x,y),axis=0) #concatenate 함수는 배열을 병합할때 사용
# axis 는 병합할 방향을 지정함 
z1= np.concatenate((x,y),axis=1)
print(z)
print(z1)

# 배열을 분리하는 방법

a = np.array([1,2,3,4,5,6])
b,c = np.split(a,[4],axis=0)
print(b,c)

# array 의 모양과 크기 

#np.zeros(): 모든 원소가 0인 배열을 생성합니다.
# np.ones(): 모든 원소가 1인 배열을 생성합니다.
# np.arange(): 범위 내의 일정 간격을 가진 배열을 생성합니다.
# np.linspace(): 범위 내에서 균등 간격으로 원하는 개수의 배열을 생성합니다.
# np.random.random(): 0부터 1사이의 난수를 가지는 배열을 생성합니다.
# np.random.randn(): 평균이 0이고 표준편차가 1인 정규 분포를 따르는 난수를 가지는 배열을 생성합니다.

arr =np.arange(1,11,3) # 범위내의 일정 간격을 가진 배열 생성
print(arr)

lins_arr = np.linspace(0,2,10)
print(lins_arr)

# 넘피의 난수 함수 
# seed() : 난수 발생기의 seed를 지정한다.
# permutation() : 임의의 순열을 반환한다.
# shuffle() : 리스트나 배열의 순서를 뒤섞는다.
# rand() : 균등분포에서 표본을 추출한다.
# randint() : 주어진 최소/최대 범위 안에서 임의의 난수를 추출한다.
# randn() : 표준편차가 1이고 평균값이 0인 정규분포에서 표본을 추출한다.
# binomial() : 이항분포에서 표본을 추출한다.
# normal() : 정규분포(가우시안)에서 표본을 추출한다.
# beta() : 베타분포에서 표본을 추출한다.
# chisquare() : 카이제곱분포에서 표본을 추출한다.
# gamma() : 감마분포에서 표본을 추출한다.
# uniform() : 균등(0,1)에서 표본을 추출한다.
