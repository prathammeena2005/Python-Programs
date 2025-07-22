import csv
with open ("employeedata.csv","a") as f:
    data=csv.writer(f)
    data.writerow(['Employee ID','Name','Salary'])
    num=int(input("Enter number of students you want to add: "))
    for i in range(num):
        id=int(input("Enter Employee Id: "))
        name=input("Enter name: ")
        sl=int(input("Enter salary: "))
        rec=[id, name, sl]
        data.writerow(rec)
