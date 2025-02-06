# 함수에 대해서 공부하기


def add(a, b):
    return a + b


print(add(1, 2))

# 간단한 더하기 함수 만들어보기
# 변수로 받는 인자값에 * 를 하는 이유는 가변 인수를 만들기 위함.
# 가변 인자값은 튜플로 저장된다.


def add_num(*args):
    result = 0
    for arg in args:
        result += arg
    return result


print(add_num(
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
), end=' ')

# 람다 함수 사용법
add = lambda a, b: a * b
result = add(3, 4)
print('결과는', result)
