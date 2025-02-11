#  09filepickle.py

import pickle
import time
fileName ='./mydata.pckf'

menu ={
    'name': 'coffee',
    'price': 2300,
    'kind': ['아이스','라떼','카푸치노']
}

with open(fileName,'wb') as myfile:
    pickle.dump(menu,myfile)

print('피클 파일 저장 구현 했습니다')
print('피클파일 오픈구현 처리 확인')
print('- ' * 30)
time.sleep(2)

file = open(fileName, 'rb')
mydata = pickle.load(file)
print(mydata)

print('피클파일 오픈처리')