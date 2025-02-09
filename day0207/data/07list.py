# 07 list.py


# 리스트 끼리 +
# 마지막 위치에 리스트 2가 더해진다.
list1 = [11,22,33,44]
list2 = [55,66]

list3 = list1 + list2 
print(list3)

print()
#리스트 * 

list1 = [1,2,3,4]
list4 = list1 * 2
print(list4)

# 슬라이싱 문법 

a_list =[1,2,3,4,5,6,7]
a= a_list[1:4] # 2,3,4
print(a)

a= a_list[:5]
print(a)

a= a_list[::-1] # 마지막부터 가져오기
print('[::-1]',a)

# list 를 튜플로 만드는 이유
#  튜플은 내부의 값의 요소를 변경할 수 없기 때문에
# 변경하면 안되는 data들을 튜플로 관리한다

list2 = [1,2,3,4,5]
list2 = tuple(list2)
print(list2,'list 2222')