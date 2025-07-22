class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius**2
    
    def perimeter(self):
        return 2*3.14*self.radius
    
c1=Circle(4)
print("Area of circle =", c1.area())
print("Perimeter of circle =", c1.perimeter())