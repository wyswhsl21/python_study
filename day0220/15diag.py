import numpy as np  


# 대각 실습 eye
# 대각 실습 diag

a = np.eye(4,6)
print(a)
print()

b = np.diag( [9,3,7,3,6,4] ) 
print(b)
print()

#멘토님     대각선을 뜻하는 diagnal -> diag  다이에그 라고 읽는게 맞습니다
#현태조장님 코파일은 다이애그 
x = np.array( [
    [1,2,3,4,5,6],
    [6,5,4,3,2,1],
    [11,12,13,14,15,16],
    [76,75,74,73,72,71],
    [86,85,84,83,82,81],
    [96,95,94,93,92,91]
  ] )
print(x)
print()

print( np.diag(x)  ) #x의 대각선 값 추출 [ 1  5 13 73 82 91]
print()

#멘토님     대각선을 뜻하는 diagnal -> diag  다이에그 라고 읽는게 맞습니다
#현태조장님 코파일은 다이애그 