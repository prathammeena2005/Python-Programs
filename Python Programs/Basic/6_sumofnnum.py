num=int(input("Enter a number: "))
sum=0
if num>0:
    for i in range(num, 2*num+1):
        sum+=i
elif num<0:
    for i in range(2*num, num+1):
        sum+=i
else:
    print("You entered 0.")
print(sum)  