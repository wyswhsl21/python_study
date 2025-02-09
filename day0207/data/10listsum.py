# 10listsum.py

# 초기값 10 숫자 10개 range() 이용 발생 , append(), insert(위치 , 값)
# for 반복문 data리스트 출력 
data =[]
for i in range(1,11):
   data.append(i)


print(data,sum(data))