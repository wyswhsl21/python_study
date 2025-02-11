# 03 fiilewrite.py

path ='emp.txt'
with open('./emp.txt','a', encoding='utf-8') as myfile:
    name = input('닉이름 입력 :')
    pay = input('급여 입력 :')
    myfile.write(name + '\n')
    myfile.write(pay + '\n')
    myfile.close()

print(path, '파일저장 테스트 11:43 1:15')