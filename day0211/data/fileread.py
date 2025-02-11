# 
path ='abc.txt'
file = open('./abc.txt','r',encoding='utf-8')
data = file.read()
print(data)
file.close()
print(path,'파일 읽기 테스트')