import math
import numpy as np

my = [175, 177, 179, 181, 183]

# 문제 1최댓값
# 최소 값
# 중앙 값
# 총점
# 평균

# np 로 처리하는 방법법
val = np.array(my)
val_max = np.max(my)
val_min = np.min(my)
val_avg = np.mean(my)
val_total = np.sum(my)
val_std = np.std(my)  # 표준편차 구하는 방식
val_median = np.median(my)
val_var = np.var(my)

# 평균계산
mean = sum(my) / len(my)
#분산 계산 = 데이터 값 - 편차

variance = sum((x - mean)**2 for x in my) / len(my)

#표준편차 계산
std_dev = variance**0.5

print('- ' * 30)

print(f' numpy 분산 계산 ={val_var} 수식으로 만든 분산 계산 {variance}')
print()
print(f'표준편차 계산 = {std_dev} 넘피 표준편차 계산 {val_std}')
'''
한줄 요약
분산(variance): 데이터가 평균에서 얼마나 퍼져 있는지 측정
✅ 편차(deviation): 데이터 값에서 평균을 뺀 값
✅ 표준 편차(standard deviation): 분산의 제곱근, 실제 데이터와 같은 단위를 가짐
✅ 제곱하는 이유: 음수 값을 없애고, 평균 편차의 합이 0이 되는 문제를 해결하기 위해


1. 분산이란?
분산(variance)은 데이터가 평균을 중심으로 얼마나 퍼져 있는지를 나타내는 값이야.
즉, 데이터 값들이 평균과 얼마나 차이가 나는지를 제곱하여 평균을 구한 값이라고 보면 돼.

분산이 크면 데이터 값들이 평균에서 멀리 퍼져 있다는 뜻이고,
분산이 작으면 데이터 값들이 평균 근처에 몰려 있다는 뜻이야.
수식으로 표현하면, **모집단의 분산(σ², sigma squared)**은 다음과 같이 정의돼:


'''
