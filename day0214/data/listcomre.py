# 리스트 컴프리헨젼



message = [14,15,243,25,1234,236,457,345,423,6453,354,23,564,2345]
print(f'{[i for i in message if i%2 != 0]}')

message = ['spam','ham','spam','ham','spam']

p = list(map(lambda x:1 if x == 'spam' else 0,message)) #람다 활용

s = [1 if i == "spam" else 0 for i in message] #리스트 컴프리헨젼

number_list = []
for i in message:
    if i =='spam':
        number_list.append(1)
    else:
        number_list.append(0)
print(number_list,'list출력')


print()       
print(p)
print(s,end=' ')