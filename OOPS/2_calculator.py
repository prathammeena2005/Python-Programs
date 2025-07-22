class Calculator:
    def __init__(self,num):
        self.square=num**2
        self.cube=num**3
        self.sq_root=num**1/2
n=Calculator(5)
print("Square =",n.square)
print("Cube =",n.cube)
print("Square root =",n.sq_root)