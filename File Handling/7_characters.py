f1= open("LOWER.txt","a")
f2=open("UPPER.txt","a")
f3=open("OTHERS.txt","a")
ans='y'
while ans=='y':
    c=input("Enter character: ")
    if c.islower():
        f1.write(c+'\n')
    elif c.isupper():
        f2.write(c+'\n')
    else:
        f3.write(c+'\n')
    ans=input("Want to enter character(y/n): ")
f1.close()
f2.close()
f3.close()