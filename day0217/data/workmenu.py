# workmenu.py
'''
- 딕트 등록,전체출력,수정,삭제,검색, 프로그램종료
- 반복문,제어
- 입력,형변환
'''

import sys

menu = {}
flag = True
num = 9  #정수형 9이면 프로그램종료 

def dictNewAdd():
    print('dictNewAdd() 사용자정의 함수영역')
    name = input('메뉴이름입력? ') #key항목 
    price = int(input('메뉴가격입력? ')) #value항목 
    menu[name] = price #딕트에 목록등록
    print(f'{name}딕트등록 성공했습니다')
    #파일처리 추가 

def dictAllprint():
    print('dictAllprint() 사용자정의 함수영역')
    for k in menu:
      print(k, ':' , menu[k] )

def dictEdit():
    print('dictEdit() 사용자정의 함수영역')
    name = input('수정메뉴이름 입력? ')
    if menu.get(name) == None :
      print(name, '수정항목 메뉴key 없습니다')
    else:
      price = int(input('수정 가격입력? ')) 
      menu[name] = price #기존내용 딕트수정처리 
      print(name,'수정처리 성공했습니다')

def dictDelete():
    print('dictDelete() 사용자정의 함수영역')
    name = input('삭제메뉴이름 입력? ')
    if menu.get(name) == None :
      print(name, '삭제항목 메뉴key 없습니다')
    else:
      menu.pop(name)
      print(name,'삭제처리 성공했습니다')

def dictSearch():
    print('dictSearch() 사용자정의 함수영역')
    name = input('검색메뉴이름 입력? ')
    if menu.get(name) == None :
      print(name, '항목 메뉴key 없습니다')
    else:
      print(name, ':', menu[name])

def dictExit():
   print('dictExit() 사용자정의 함수영역') 
   print('프로그램을 종료합니다\n') 
   sys.exit()


while flag:
  print()
  print('1.등록  2.전체출력  3.수정  4.삭제  5.검색  9.종료 ')
  num = int(input('>>> '))
  if num == 1:     dictNewAdd()
  elif num == 2 :  dictAllprint()
  elif num == 3 :  dictEdit()
  elif num == 4 :  dictDelete()
  elif num == 5 :  dictSearch()
  elif num == 9 :  dictExit()
  else :
    print('번호를 잘못 입력 했습니다\n')

# 항상 함수는 상단에 먼저 기술=구현=정의 한후 
# 아래에서 호출이 정답 