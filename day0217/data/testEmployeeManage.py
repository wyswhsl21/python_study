class Employee:

    def __init__(self, emp_id, name, pay):
        self.emp_id = emp_id
        self.name = name
        self.pay = pay

    def display(self):
        print(f'아이디: {self.emp_id}  이름: {self.name} 급여: {self.pay}')

    def update_pay(self, new_pay):
        self.pay = new_pay
        print(f'{self.name}님 월급이 {self.pay}로 변경되었습니다.')


object1 = Employee(2025101, '김연아', 7000)
object2 = Employee(2025102, '손흥민', 4500)

object1.display()
object2.display()

#월급수정
object1.update_pay(9700)
print()


class EmployeeManager:
    mylist = []

    def add_employee(self, emp_id, name, pay):
        employee = Employee(emp_id, name, pay)
        self.mylist.append(employee)
        print(f'{name} 사원님 추가 되었습니다.')

    def display_all_employees(self):
        if not self.mylist:
            print('현재 직원이 없습니다.')
            return
        print('\n전체직원출력')
        for emp in self.mylist:
            emp.display()

    def find_employee_by_id(self, emp_id):
        for emp in self.mylist:
            if emp.emp_id == emp_id:
                print('\n---------- 검색된 직원 정보 -----------')
                emp.display()
                return
        print(f'\n{emp_id}사번의 직원을 찾을 수 없습니다.')


manager = EmployeeManager()
manager.add_employee(101, '페이커', 5000)
manager.add_employee(102, '고길동', 4000)
manager.add_employee(103, '유재석', 3500)

manager.display_all_employees()
manager.find_employee_by_id(200)
