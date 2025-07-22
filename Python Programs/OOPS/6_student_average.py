class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    
    def get_average(self):
        s=self.marks1+self.marks2+self.marks3
        print("Student name is",  self.name, "average =",s/300)

s1=Student("Armaan", 75, 68.25, 82.5)
s1.get_average()