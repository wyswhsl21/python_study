import pickle
import os.path
import sys
fname_pck ='./mydata.pckf'
fname_txt = './mydata.txt'
num = 9
menu = dict()
flag = True

def menu_open():
    print('1.피클 쓰기','2.파일 쓰기','3.피클 읽기', '4. 파일 읽기', '9. 종료')
    open_data = input(':')
    return open_data
def menu_1():
    try:
        if os.path.exists(fname_pck):
            with open(fname_pck,'rb') as mypck:
                try:  
                    data = pickle.load(mypck) 
                    if not isinstance(data,list):
                        data=[]
                except EOFError:
                    data = []
        else:
            data=[]
        print(data,'데이터')
        new_data = input('피클에 저장할 글을 입력하시오.\n>>>')
        data.append(new_data)
        print('새로운 데이터',data)
        with open(fname_pck,'wb') as newpck:
            pickle.dump(data,newpck)

        print('피클에 정상적으로 저장 하였습니다.')

    except Exception as e:
        print(e)
def menu_2():
    file_data = input('파일에 저장할 글을 입력하시오\n>>>')
    with open(fname_txt,'a',encoding='utf-8')as mytxt:
        mytxt.write(file_data + '\n')
        mytxt.close()
def menu_3():
    try:
        save_path = os.path.abspath(fname_pck)
        if not os.path.exists(save_path):
            print('피클 이름이 존재하지 않습니다.')
        else:
            with open(save_path,'rb') as mypck:
                pck_data =pickle.load(mypck)
            print(pck_data)
            print('- ' * 30)
    except Exception as e:
        print(f'에러에 대한 내용은 {e} 입니다.')
def menu_4():
    try:
        save_path = os.path.abspath(fname_txt)
        if not os.path.exists(save_path):
            print(f'파일 이름이 존재하지 않습니다.')
        else:
            with open(save_path,'r',encoding='utf-8') as mytxt:
                myfile_data = mytxt.readlines()
                print(myfile_data)
        pass
    except Exception as e:
        print(f'에러에 대한 내용은 {e} 입니다.')
def menu_exit():
    sys.exit()



while True:
    menu = menu_open()
    print(menu)
    if menu == '1':
        menu_1()
    elif menu =='2':
        menu_2()
    elif menu == '3':
        menu_3()
    elif menu == '4':
        menu_4()
    elif menu == '9':
        menu_exit()
    else:
        print('정확한 숫자를 입력해주세요')
    




