def test():
    kor, eng, total, avg = 0, 0, 0, 0
    message = '결과'

    kor = int(input('국어 점수를 입력하시오'))
    eng = int(input('영어 점수를 입력하시오'))
    if kor is not None and eng is not None:
        total = kor + eng
    else:
        print('값을 입력해주시오오')
    avg = total // 2
    if avg >= 70:
        message = '축합격'
    else:
        message = '재시험'
    return (total, avg, message)


if __name__ == '__main__':
    x, y, z = test()
    print(f'총점 = {x}')
    print(f'평균 = {y}')
    print(f'학점 결과 = {z}')
