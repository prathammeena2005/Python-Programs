num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
def min_onesdigit(num1,num2):
    a=num1%10
    b=num2%10
    if a<b:
        return num1
    else:
        return num2
result= min_onesdigit(num1,num2)
print("Number with minimum one's digit=",result)