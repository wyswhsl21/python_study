# calculator2.py

result1 = 0
result2 = 0


def add1(num):
    global result1  #global 함수는 지역변수를 따로 만들지 않고 전역변수 result1 을 사용하겠다는 의미이다.
    result1 += num
    return result1


def add2(num):
    global result2
    result2 += num
    return result2


print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))


class Calculator:

    def _init_(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result
