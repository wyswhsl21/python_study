# class


class Emp:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def insert(self):
        print(f'insert함수,{self.name} {self.age}')


print('2-14 금요일 클래스 실습')

if __name__ == '__main__':
    my = Emp('kim', 45)
    print(my)
    my.insert()
