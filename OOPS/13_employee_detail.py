class Employee:
    def __init__(self, role, department, salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetail(self):
        print("Role :", self.role)
        print("Department :", self.department)
        print("Salary :", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name=name
        self.age=age
        super().__init__("Engineer", "IT", 65000)

    def showDetail(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Role :", self.role)
        print("Department :", self.department)
        print("Salary :", self.salary)


e1=Employee("Accountant", "Finance", 60000)
e1.showDetail()
e2=Engineer("Alex",28)
e2.showDetail()