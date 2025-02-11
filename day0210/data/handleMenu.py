# 메뉴 활성화 함수
import sys
class MenuFunc:
    def __init__(self):
        self.menu = {}

    def menu_open(self):
        print('\n1.등록 2.전체출력 3. 수정 4.삭제 5. 검색 9.종료')
        num= input('>>>')
        return num
    def insert_menu(self):
        name = input('메뉴입력:')
        price = int(input('가격입력:'))
        self.menu[name] = price #딕트 등록 처리
        print(f'{name} 메뉴가 등록 되었습니다.')
    def read_menu(self):
        print('모든 메뉴를 출력합니다')
        if not self.menu:
            print('현재 등록된 메뉴가 없습니다.')
        for name,price in self.menu.items():
            print(f'{name}:{price}원')
    def update_menu(self):
            change_name = input('수정할 메뉴를 입력해주세요:')
            if change_name in self.menu:
                new_price = int(input('수정할 가격을 입력해주세요 :'))
                self.menu[change_name] = new_price
                print(f'{change_name} 메뉴의 가격이 {new_price}원으로 수정되었습니다.')
            else:
                print('해당 메뉴가 존재하지 않습니다.')
    def delete_menu(self):
        pop_data = input('삭제할 data를 입력해주세요 :')
        if pop_data in self.menu:
            self.menu.pop(pop_data)
            print(f'선택한 {delete_data} data가 삭제 되었습니다')
        else:
            print('해당 메뉴가 존재하지 않습니다.')
    def search_menu(self):
            serch_keyword = input('검색할 메뉴를 입력해주세요.')
            if serch_keyword in self.menu:
                print(f'검색 결과 가격은 : {self.menu[serch_keyword]}')
            else: print('현재 메뉴에 존재하지 않습니다.')   
    def exit_menu(self):
            print('\n프로그램을 종료합니다.')
            sys.exit()
        