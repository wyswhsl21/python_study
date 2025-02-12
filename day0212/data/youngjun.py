import sys

hotel_room = {}

def crRoomList():
    for floor in range(1, 4):  # 1층~3층
        rooms = {}  # 각 층별로 새로운 딕셔너리 생성
        for room in range(1, 6):  # 각 층에 5개의 방
            room_num = floor * 100 + room  # 방 번호 (101~105, 201~205, 301~305)
            rooms[room_num] = None  # 처음엔 빈 방
        hotel_room[floor] = rooms  # 층별 방 저장


def checkIn(room_num):
    floor = room_num // 100  
    if floor in hotel_room and room_num in hotel_room[floor]:
        if hotel_room[floor][room_num] is not None:
            return f'죄송합니다. {room_num}방은 이미 예약되었습니다.'
        else:
            guest_name = input('성함을 입력해주세요: ')
            print(hotel_room[3],'listtt ?')
            hotel_room[floor][room_num] = guest_name  # 손님 배정
            return f'{guest_name}님, {room_num}방으로 입실 처리되었습니다.'
    else:
        return '해당 방 번호는 존재하지 않습니다.'


def checkOut(room_num):
    floor = room_num // 100  
    if floor in hotel_room and room_num in hotel_room[floor]:
        if hotel_room[floor][room_num] is None:
            return f'{room_num}방은 이미 비어있습니다.'
        else:
            guest_name = hotel_room[floor][room_num]
            hotel_room[floor][room_num] = None  # 방을 비움
            return f'{guest_name}님, {room_num}방에서 퇴실 처리되었습니다.'
    else:
        return '해당 방 번호는 존재하지 않습니다.'


def viewStateRoom():
    print("★ 그랜드 부다페스트 방문을 환영합니다 ★")
    for floor, rooms in sorted(hotel_room.items()):
        room_line = []
        name_line = []
        
        for room_num, guest in sorted(rooms.items()):
            print(room_num , 'room num 데이터', guest)
            room_line.append(f"{room_num:>5}")  # 방 번호 정렬
            name_line.append(f"{guest if guest else '':>5}")  # 손님 이름 (없으면 공백)

        print(" ".join(room_line))
        print(" ".join(name_line))
        print("-" * 40)


if __name__ == '__main__':
    crRoomList()  # 호텔 객실 초기화

    while True:
        print('\n1. 입실  2. 퇴실  3. 전체출력  9. 종료')
        try:
            num = int(input('원하시는 작업 번호를 입력해주세요: '))
        except ValueError:
            print('올바른 숫자를 입력하세요.')
            continue

        if num == 1:
            room_num = int(input('방번호를 적어주세요: '))
            print(checkIn(room_num))
        elif num == 2:
            room_num = int(input('방번호를 적어주세요: '))
            print(checkOut(room_num))
        elif num == 3:
            viewStateRoom()
        elif num == 9:
            print('프로그램을 종료합니다. 감사합니다.')
            sys.exit()
        else:
            print('다시 입력해주세요.')