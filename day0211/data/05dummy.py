# 
path ='./data/dummy.txt'
with open(path,'r',encoding='utf-8') as myfile:
    data = myfile.readlines()
    print(data)
    myfile.close()
# print(path,'파일 읽기 테스트')

# myfile.read 
# myfile.readline
# myfile.readlines
