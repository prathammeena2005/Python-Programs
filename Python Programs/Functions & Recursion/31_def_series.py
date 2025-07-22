num1=int(input("Enter first number: "))
num2=int(input("Enter last number: "))
def series(first,last):
    for i in range(first,last):
        diff=(last-first)//3
        series=[first,first+diff,first+2*diff,last]
        return series
sol=series(num1,num2)
print("Generated Series:", sol)