'''
2차원 구조 리스트
2차원 for, 입력 input(), 형변환
복합데이터 [[],[]] [{},{}] {key:손님}
파일처리저장, 읽기 처리 구현x , 정규식 x
함수구현 더 적절 checkIn(), checkOut()
'''
# 메뉴 오픈 함수

def check_menu_open():
    open_menu_num =input('1.입실 2.퇴실 3.전체출력 4.전체출력2 9.종료 >>>')
    return open_menu_num

#전체출력 기능 1
def print_hotel(guest_data):
    try:
        print(guest_data,'dataaaaa')
        print('★그랜드 부다페스트 방문을 환영합니다★ ')
        hotel_room =[[101,102,103,104,105],[201,202,203,204,205],[301,302,303,304,305]]
     
        for floor in range(len(hotel_room)):
            for room_num in range(len(hotel_room[floor])):
                
                print(hotel_room[floor][room_num], end='\t')
            print()
            for check_in in range(len(guest_data[floor])):
                print(f'{guest_data[floor][check_in]:^2}',end ='\t')
            print()
            print('- '*20,end='\n')  
    except Exception as e:
        print(f'예상치 못한 오류 발생 {e}')

#전체출력 기능 2
def print_hote_num2(guest_data):
    try:
        print('★그랜드 부다페스트 방문을 환영합니다★ ')
        hotel_room =[[101,102,103,104,105],[201,202,203,204,205],[301,302,303,304,305]]
        for floor in range(len(hotel_room)):
        
            for room_num in range(len(hotel_room[floor])):                
                print(hotel_room[floor][room_num], end='\t')
                if guest_data[floor][room_num] == '':
                    print(f'{'□'.lstrip():<2}{guest_data[floor][room_num].rstrip()}',end='\t')
                else:
                    print(f'{'■'.lstrip():<2}{guest_data[floor][room_num].rstrip()}',end='\t')
               
            print() 
            
            print('- '*40,end='\n')  
    except Exception as e:
        print(f'예상치 못한 오류 발생 {e}')

#호텔 체크인 함수 
def check_in(data):
    try:

        check_floor = input('몇층 입실>>>')
        check_floor = int(check_floor)
        if (check_floor) > 3 or check_floor <1 :
            print('다시 한번 확인해주세요. 저희 호텔은 최대 3층 룸은 5호실까지 있습니다.')
            return
        
        check_room_num = input('몇호 입실>>>')
        check_room_num = int(check_room_num)
        if (check_room_num) > 5 or check_room_num == 0:
            print('다시 한번 확인해주세요. 저희 호텔은 최대 3층 룸은 5호실까지 있습니다.')
            return

        check_guest_name = input('고객 이름>>>')
    
        floor_idx =check_floor -1
        room_idx = check_room_num -1
        if data[floor_idx][room_idx] == '' or data[floor_idx][room_idx] == check_guest_name:
            data[floor_idx][room_idx] = check_guest_name
            print('해당 객실로 체크인 되었습니다. 이용해주셔서 감사합니다.')
        else:
            print('해당 객실 호수는 다른 손님이 이용중입니다.\n전체 출력 후 비어있는 객실 이용 바랍니다.')
    except Exception as e:
        print(f'예기치 못한 오류 발생 {e}')


def check_out(data):
    try:
        out_floor = input('몇층 퇴실>>>')
        out_floor = int(out_floor)
        if (out_floor) > 3 or out_floor <1 :
            print('다시 한번 확인해주세요. 저희 호텔은 최대 3층 룸은 5호실까지 있습니다.')
            return
        
        out_room_num = input('몇호 퇴실>>>')
        out_room_num = int(out_room_num)
        if (out_room_num) > 5 or out_room_num == 0:
            print('다시 한번 확인해주세요. 저희 호텔은 최대 3층 룸은 5호실까지 있습니다.')
            return

        out_guest_name = input('고객 이름>>>')
    
        floor_idx =out_floor -1
        room_idx = out_room_num -1
        if data[floor_idx][room_idx] == out_guest_name:
            data[floor_idx][room_idx] = ''
            print('체크아웃 되었습니다. 이용해주셔서 감사합니다.')
        else:
            print('이용하신 손님 이름과 일치 하지 않습니다.',data[floor_idx][room_idx], out_guest_name)
            
    except Exception as e:
        print(f'예기치 못한 오류 발생 {e}')



data =[['','','','',''],['','','','',''],['','','','','']]
while True:
    num = check_menu_open()
    if num == '1':
        check_in(data)
    elif num =='2':
        check_out(data)
    elif num == '3':
        print_hotel(data)
    elif num == '4' :
        print_hote_num2(data)
    elif num == '9' :
        print('시스템을 종료하겠습니다.')
        break
    else:
        print('올바른 번호를 입력해주세요!!')