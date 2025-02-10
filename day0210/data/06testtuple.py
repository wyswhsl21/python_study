# 05 testtuple.py

mytuple = (
    '제주',
    37.75148,
    126.34136,
    '시청',
)  # 튜플
print(mytuple)

#문제 1번 튜플 항목추가 '인천'
new_tuple = mytuple + ('인천', )
print('추가 된 튜플', new_tuple)
# 방법 2 리스트로 만들고 추가 후 다시 튜플로 변경
new_tuple1 = list(mytuple)
new_tuple1.append('인천')
new_tuple1 = tuple(new_tuple1)
print('추가된 튜플', new_tuple1)
# enumerate

for i, e in enumerate(mytuple):
    print(i, ':', e)

# 문제 data 리스트를 for 반복문으로 출력

datas = ['제주', 34.56756, '시청', 36.73982]  #리스트
#문제 2 리스트 항목 추가 '성남'
datas.append('성남')

for value in range(len(datas)):
    print(i, ':', datas[value])
