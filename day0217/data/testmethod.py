def dic_method(**p):
    for i in p.keys():
        print(i, ':', p[i])

    print()


dic_method(code=1200, title='aaa', flag=False)



def menu_method(menu):
    print(f'code: {menu['code']}')
    print(f'code: {menu['title']}')
    print(f'code: {menu['flag']}')
    print()

menu={'code':7800,'title':'bbbb','flag':False}

menu_method(menu)