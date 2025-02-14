import os
import re

file_path = "./data/sukjae"
os.makedirs("./data", exist_ok=True)

rooms = {}
try:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                m = re.match(r"(\d+):(.+)", line.strip())
                if m:
                    rooms[m.group(1)] = m.group(2)
except Exception as e:
    print(f"파일 읽기 중 오류 발생: {e}")

def validate_input(prompt, pattern):
    while True:
        value = input(prompt).strip()
        if re.fullmatch(pattern, value):
            return value.zfill(2) if pattern == r"(0[1-5]|[1-5])" else value
        print("잘못된 입력입니다.")

def check_in():
    try:
        floor = validate_input("> 몇층 입실>>> ", r"[1-3]")
        room_num = validate_input("> 몇호 입실>>> ", r"(0[1-5]|[1-5])")
        name = input("> 고객 이름>>> ").strip()
        room_id = floor + room_num
        if room_id in rooms:
            print("해당 객실은 이미 예약되었습니다.")
        else:
            rooms[room_id] = name
            print(f"체크인 완료 ({room_id}호: {name})")
    except Exception as e:
        print(f"입실 처리 중 오류 발생: {e}")

def check_out():
    try:
        floor = validate_input("> 몇층 퇴실>>> ", r"[1-3]")
        room_num = validate_input("> 몇호 퇴실>>> ", r"(0[1-5]|[1-5])")
        room_id = floor + room_num
        if room_id in rooms:
            del rooms[room_id]
            print("체크아웃 완료")
        else:
            print("해당 객실이 존재하지 않습니다.")
    except Exception as e:
        print(f"퇴실 처리 중 오류 발생: {e}")

def menu():
    while True:
        print("\n1.입실 2.퇴실 3.전체출력1 4.전체출력2 9.종료 >>> ", end="")
        choice = input().strip()
        if choice in ['1', '2', '3', '4', '9']:
            return choice
        print("잘못된 입력입니다.")

def all_display():
    try:
        print("\n★ 그랜드 부다페스트 방문을 환영합니다 ★\n")
        col_width = 8
        for floor in ['1', '2', '3']:
            room_numbers = [floor + room for room in ['01', '02', '03', '04', '05']]
            print("".join(f"{room:^{col_width}}" for room in room_numbers))
            print("".join(f"{rooms.get(room, '')[:col_width]:^{col_width}}" for room in room_numbers))
            print("-" * (col_width * 5))
    except Exception as e:
        print(f"전체 출력 중 오류 발생: {e}")

def all_display2():
    try:
        print("\n★ 객실 현황 ★\n")
        for floor in ['1', '2', '3']:
            rooms_display = []
            for room_num in ['01', '02', '03', '04', '05']:
                room_id = floor + room_num
                status = "■" if room_id in rooms else "□"
                display = f"{room_id}호 {status}"
                if room_id in rooms:
                    display += f" {rooms[room_id]}"
                rooms_display.append(display)
            print("  ".join(rooms_display))
            print()
    except Exception as e:
        print(f"전체 출력2 중 오류 발생: {e}")

while True:
    try:
        choice = menu()

        if choice == '1':
            check_in()
        elif choice == '2':
            check_out()
        elif choice == '3':
            all_display()
        elif choice == '4':
            all_display2()  
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.writelines(f"{room}:{name}\n" for room, name in rooms.items())
                print("프로그램 종료")
                break
            except Exception as e:
                print(f"파일 저장 중 오류 발생: {e}")

    except Exception as e:
        print(f"프로그램 실행 중 오류 발생: {e}")