num=int(input("Enter a number: "))
if num<0:
    print("Factorial of negative number is not defined")
elif num==0:
    print("Factorial of 0 is 1")
else:
    product=1
    for i in range (1,num+1):
        product*=i
    print('Factorial of', num,'is',product)
    