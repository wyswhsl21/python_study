class Emp:

    def insert(self, name):
        print('Emp insery 함수', name)
        self.name = name

    def printAll(self):
        print('Emp printAll', self.name)
        print()


ob = Emp()
ob.insert('길동')
ob.printAll()
