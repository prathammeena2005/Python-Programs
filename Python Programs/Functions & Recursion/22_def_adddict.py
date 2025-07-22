d1=eval(input("Enter first dictionary: "))
d2=eval(input("Enter second dictionary: "))
def addDict(dict1,dict2):
    d={}
    for i in dict1:
        d[i]=dict1[i]
    for j in dict2:
        d[j]=dict2[j]
    return d
print("Union of dict1 and dict2:", addDict(d1,d2))