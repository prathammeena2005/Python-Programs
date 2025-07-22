num=int(input("Enter a positive number: "))
prime=True
if num<0:
    print("You entered a negative number")
elif num==0 or num==1:
    print("Enter another numbere ")
else:
    for i in range(2,num):
        if num%i==0:
            prime=False
            break   
if prime==True:
    print(num, 'is a prime number')
else:
    print(num, 'is not a prime number')
        