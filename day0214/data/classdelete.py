class Emp:
    name = ''
    age = 0
    address = ''

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def emp_print(self):
        print(f'내 이름은 {self.name} 이고 나이는 {self.age} 이고 주소는 {self.address}')

    def emp_delete(self):
        pass


if __name__ == '__main__':
    my = Emp('jaewoo', 31, '선수촌로 8')
    my.emp_print()
