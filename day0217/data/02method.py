def estsoft_method(menu):
    print(f'code : {menu['code']}')
    print(f'title: {menu['title']}')
    print(f'Flag : {menu['flag']}')
    print()


menu = {'code': 7700, 'title': 'blue', 'flag': False}
estsoft_method(menu)  # 함수의 매개인자 갯수가 틀려도 실행 가능 , 타입이 달라져도 호출한 인자 그대로 들어감.
