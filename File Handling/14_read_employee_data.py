import csv
with open ("employeedata.csv","r") as f:
    data=csv.reader(f)
    for i in data:
        print(i)
        
