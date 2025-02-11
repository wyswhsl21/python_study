# filewrite.py
path = './day0211/data/abc.txt'
file = open('./day0211/data/abc.txt', 'w', encoding='UTF-8')
name = input('이름 입력 : ')
age = input('나이 입력 : ')
file.write(name + '\n')
file.write(age + '\n')
file.close()
print(path, '파일저장 테스트')
