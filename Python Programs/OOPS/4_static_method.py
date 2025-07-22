class Calculator:
    def __init__(self,num):
        self.square=num**2
        self.cube=num**3
        self.sq_root=num**1/2

    @staticmethod
    def greet():
        print("Hello,\nWelcome!")
n=Calculator(5)
n.greet()
print("Square =",n.square)
print("Cube =",n.cube)
print("Square root =",n.sq_root)