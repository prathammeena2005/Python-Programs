import random
num1=int(input("Enter 1st no.: "))
num2=int(input("Enter 2nd no.: "))
def randomno(n1,n2):
    a=random.randint(n1,n2)
    return a
for i in range(3):
    b=randomno(num1,num2)
    print("Random number in range",num1,'and', num2,':', b )