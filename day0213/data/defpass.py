'''
함수 정의
함수 mypass

매개인자 kor ,eng 키보드 입력 예외처리 try ~ except
리턴값은 평균값으로 70점부터 ~ 100 합격, 0~69점 재시험


'''


def mypass(*sub):
    try:
        subSum = sum(sub)
        avg = subSum // len(sub)
        message = ''
        if avg >= 70 and avg <= 100:
            message = '합격'
        else:
            message = '불합격'
        return message
    except Exception as e:
        print(f'오류가 발생했습니다 오류는 {e}')


if __name__ == '__main__':
    kor = int(input('국어점수를 입력해주세요>>>'))
    eng = int(input('영어점수를 입력해주세요>>>'))
    res = mypass(kor, eng)
print(f'시험결과는 {res} ')
