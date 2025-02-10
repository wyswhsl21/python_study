import handleMenu 

if __name__ == '__main__':
    menu =handleMenu.MenuFunc()


while True :
    choice = menu.menu_open()

    try:
        if choice == '1':
            menu.insert_menu()
        elif choice == '2':
            menu.read_menu()
        elif choice == '3':
            menu.update_menu()
        elif choice == '4':
            menu.delete_data()
        elif choice == '5':
            menu.search_data()
        elif choice == '9':
            menu.exit_menu() 
        else:
            print('올바른 선택이 아닙니다. 다시 선택해주세요')
    except Exception as e:
        print(f'알 수 없는 오류 발생: {e}')