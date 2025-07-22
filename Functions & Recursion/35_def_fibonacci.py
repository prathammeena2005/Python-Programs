terms=int(input("Enter number of terms of Fibonacci series: "))
print("Fibonacci series= ",end='')
def fibonacci(num):
    a=0
    b=1
    count=1
    for i in range(num):
        print(a,end=' ')
        count=a+b
        a=b
        b=count
        
fibonacci(terms)