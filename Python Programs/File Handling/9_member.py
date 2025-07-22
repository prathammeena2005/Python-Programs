import pickle
def write_member():
    f = open("member.dat", 'wb')
    d={}
    a=int(input("Enter number of members: "))
    for i in range(a):
        num=int(input("Enter member no.: "))
        name=input("Enter member name: ")
        d["MemberNo"]=num
        d["Name"]=name
        pickle.dump(d, f)
    f.close()
write_member()
