import numpy as np
# 시드값을 주는 이유는 난수 발생시 같은 데이터 유지
rng = np.random.default_rng(seed=1234)
myarray = rng.standard_normal((5, 4, 2))  #5행 * 4열

print(myarray)
print('평균', myarray.mean())
print('평균', np.mean(myarray))
print('열총점', sum(myarray))
print('평균', sum(myarray))
print('전체총', np.sum(myarray))

print('myarray 정보', myarray.shape)
print('myarray 정보', myarray.size)
print('myarray 정보', len(myarray))
print('myarray 정보', myarray.ndim)  #몇 차원인지 물어보는거!
print('열', myarray.mean(axis=0))  # 열 세로
print('열', myarray.mean(axis=1))  # 행 가로로
print('열', myarray.mean(axis=2))  # 페이지지
