import random
import sys



def ai_verse_me():
    print('AI와 싸울 준비가 되었습니까?')
    options = {'1': '겨룬다', '2': '도망간다', '9': '종료'}
    print('\n'.join([f'{k}번: {v}' for k, v in options.items()]))
    return '1'  # 기본적으로 1번 선택하도록 변경

def cra_range(randomNum):
    global com
    if not com:
        com = [i for i in range(subNum, randomNum + 1)]  # 숫자 범위 생성

def start_ai_game(me):
    global com, aiCnt
    try:
        ai = random.choice(com)  # AI가 리스트에서 숫자 선택
        print(f'AI 선택: {ai}')
        if randomNum == ai:
            print(f'AI 승리! AI가 숫자 {randomNum}를 맞췄습니다!')
            return False
        else:
            return pick_ai_num(ai)
    except Exception as e:
        print(f'start_ai_game 오류: {e}')
        return True

def pick_ai_num(ai):
    global com, aiCnt
    try:
        rangeIdx = com.index(ai)
        if randomNum > ai:
            com = com[rangeIdx + 1:]
        elif randomNum < ai:
            com = com[:rangeIdx]
        aiCnt += 1
        return True
    except Exception as e:
        print(f'pick_ai_num 오류: {e}')
        return False
def my_pick_num():
    num = input('숫자를 선택해주세요. >>>')
    num = int(num)
    return num

def pick_num():
    return random.randint(1, 100)  # 사용자 입력 없이 무작위 숫자 선택

if __name__ == '__main__':
    # AI 를 이겨보기 게임
    cnt = 0  # 나의 횟수
    aiCnt = 0  # AI 횟수
    randomNum = 0  # 목표 숫자
    subNum = 1  # 최소 숫자
    flag = True  # 게임 진행 여부
    com = []  # AI가 사용할 숫자 리스트
    randomNum = random.randint(1, 100)  # 랜덤 숫자 생성
    print(f'랜덤 숫자가 정해졌습니다!')
    while flag:
        num = ai_verse_me()
        if num == '1':
            me = pick_num()
            cra_range(randomNum)
            flag = start_ai_game(me)
        elif num == '2':
            print('AI: 겁쟁이구나!')
            break
        elif num == '9':
            print('시스템을 종료합니다.')
            sys.exit()
        else:
            print('잘못된 입력입니다. 다시 선택하세요.')
