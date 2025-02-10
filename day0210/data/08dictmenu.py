# 08 dictmenu.py
'''
-첫번째 dict 를 통해서 등록, 전체 출력
- 반복문 , 제어 
- 입력, 형변환 
'''

import sys

menu = {}
flag = True
num ='9'

while flag:
    # print(menu)
    print('\n1.등록 2.전체출력 3. 수정 4.삭제 5. 검색 9.종료')
    num= input('>>>')
    if num == '1':
        name = input('메뉴입력:')
        price = int(input('가격입력:'))
        menu[name] = price #딕트 등록 처리
        print(f'{name} 딕트 등록 성공했습니다.')
    elif num == '2':
    #    for i in (menu):
        print('모두 출력합니다.')
        for k,v in menu.items():
           print(k, ':',menu[k],)
    elif num == '3':
        chage_data = input('수정할 메뉴를 입력해주세요:')
        menu[chage_data] = input('수정할 가격을 입력해주세요 :')
    elif num == '4':
        delete_data = input('삭제할 data를 입력해주세요 :')
        if delete_data in menu:
            menu.pop(delete_data)
            print(f'선택한 {delete_data} data가 삭제 되었습니다 ')
    elif num =='5':
        serch_keyword = input('검색할 메뉴를 입력해주세요.')
        if serch_keyword in menu:
            print(f'검색 결과 가격은 : {menu[serch_keyword]}')
        else: print('현재 메뉴에 존재하지 않습니다.')         
    elif num == '9':
        print('\n프로그램을 종료합니다.')
        sys.exit()
    else:
        print('번호를 잘못 입력 했습니다.')


