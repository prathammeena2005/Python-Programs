num=int(input("Enter number:"))
def sumofNnum(n):
    if (n==0):
        return 0
    return sumofNnum(n-1) + n 
s=sumofNnum(num)
print(s)