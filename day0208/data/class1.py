# calculator.py

result = 0


def add(num):
    global result
    result += num
    return result


print((add(4)))
print(add(3))
