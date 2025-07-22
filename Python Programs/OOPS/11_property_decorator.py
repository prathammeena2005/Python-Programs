class Student:
    def __init__(self, phy, chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def calcPercentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"

stu1=Student(98,87,95)
print(stu1.calcPercentage)
stu1.phy=91 
print(stu1.calcPercentage)