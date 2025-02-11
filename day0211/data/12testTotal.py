def test(kor, eng):
    total, avg = 0, 0
    message = '결과'
    grade = ''

    if kor is not None and eng is not None:
        total = kor + eng
    else:
        print('값을 입력해주시오')
    avg = total // 2
    if avg >= 70:
        message = '축합격'
    else:
        message = '재시험'

    if avg < 60:
        grade = 'F'
    elif avg < 70:
        grade = 'D'
    elif avg < 80:
        grade = 'C'
    elif avg < 90:
        grade = 'B'
    else:
        grade = 'A'

    return (total, avg, message, grade)


if __name__ == '__main__':
    kor = int(input('국어 점수를 입력하시오'))
    eng = int(input('영어 점수를 입력하시오'))
    x, y, z, grade = test(kor, eng)
    print(f'총점 = {x}')
    print(f'평균 = {y}')
    print(f'학점 결과 = {z}')
    print(f'학점 결과 = {grade}')
    
