l=[]
def multiple():
    result=0
    for i in range(1,101):
        if (i%3==0) or (i%5==0):
            l.append(i)
    print(l)
multiple()