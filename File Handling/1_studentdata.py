with open('studentdata.txt','a') as f:
    num=int(input("Enter number of student: "))
    for i in range(num):
        name=input("Enter name: ")
        roll=int(input("Enter roll no.: "))
        marks=float(input("Enter marks: "))
        data=name+','+str(roll)+','+str(marks)+'\n'
        f.write(data)