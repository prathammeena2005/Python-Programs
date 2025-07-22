class Complex:
    def __init__(self, real, img):
        self.real=real
        self.img=img

    def __add__(self,c2):
        return Complex(self.real+c2.real, self.img+c2.img)
    def __str__(self):
        return f"{self.real} + {self.img}i"

c1=Complex(1,2)
c2=Complex(4,5)
print(f"{c1.real} + {c1.img}i")
print(f"{c2.real} + {c2.img}i")
print("--------")
print(c1+c2)