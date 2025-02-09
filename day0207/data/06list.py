# 06 list.py


list1 = [20,10,40,50,30]

print(min(list1)) #가장 최솟값
print(max(list1)) #최댓 값
print(sum(list1)) #리스트의 모든 숫자 더하기

fruits = ['banana','apple','grape']
print(min(fruits)) # 알파벳 가장 먼저 순으로 출력
print(max(fruits)) # 알파벳 가장 마지막 순으로 출력

# list method 정리
# 1. insert

list1.insert(3,78) #해당 위치에 78이라는 인자값 추가
print('insert',list1)

# append 마지막 위치에 새로운 인자값 추가
list1.append(40)
print('append',list1)

# pop 마지막 위치 인덱스 삭제
list1.pop()
print('pop',list1)

# sort
list1.sort()
print('sort',list1)

list1.sort(reverse=True)
print('reverse sort',list1)

list1.reverse()
print('reverse_data',list1)

