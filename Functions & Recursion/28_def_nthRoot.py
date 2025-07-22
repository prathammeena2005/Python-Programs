x=int(input("Enter a number: "))
n=int(input("Enter number for nth root: "))
def nthRoot(x,n=2):
    root=x**(1/n)
    print(n,'th root of',x,'=',root)
nthRoot(x,n)