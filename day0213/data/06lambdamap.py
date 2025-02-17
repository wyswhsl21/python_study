# 06 lambdamap.py

for k in range(1,15):
    print(k,'목요일')

a= list(map(lambda x: x% 2,[1,2,3,4,5]))
print(a)

b= list(filter(lambda x : x%2,[1,2,3,4,5]))

print(b)

menu = [i ** j for i in range(1,6) for j in range(1,6)]
print(menu)