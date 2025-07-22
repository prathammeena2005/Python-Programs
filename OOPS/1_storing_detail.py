class Programmer:
    company="Microsoft"
    def __init__(self, name, id, salary):
        self.name=name
        self.id=id
        self.salary=salary
    
p1=Programmer("Alex",1011, 1250000)
p2=Programmer("James",1012,1500000)
print(p1.name, p1.id, p1.company, p1.salary)
print(p2.name, p2.id, p2.company, p2.salary)