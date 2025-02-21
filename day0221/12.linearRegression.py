# 단계1 ]  총합계,평균 구하기
x = [2, 4, 6, 8, 10]  #총합계 30/5   평균 6시간
y = [81, 93, 91, 97, 98]  #총합계 460/5  평균 92점
su = np.polyfit(x, y, 1)
print('선형회귀 ', su)  # 권장 결과  [1.9  80.6]
print()
# 단계2] 선형회귀 공식 y = W가중치*시간 + b편향
y_pred = np.array(x) * su[0] + su[1]
print(y_pred)  #예측값 [84.4  88.2   92.  95.8   99.6]
print()
plt.plot(x, y_pred, color='hotpink')  #예상=예측값
plt.scatter(x, y, color='red')  #실제값
plt.plot(x, y)  #line기본모양
