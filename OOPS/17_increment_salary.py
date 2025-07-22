class Employee:
    increment=0.4
    def __init__(self,salary):
        self.salary=salary

    @property
    def salaryafterIncrement(self):
        return (self.salary + (self.salary*self.increment))
    
e=Employee(20000)
print("Salary after increment =",e.salaryafterIncrement)

