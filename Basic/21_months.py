d={"January":31, "February":28, "March":31, "April": 30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}
mname=input("Enter month name: ")
days=d[mname]
print("Number of days in", mname,"are:", days)


print("Months in alphabetical order are:", sorted(d))


print("Months with 31 days are:", end=' ')
for i in d:
    if d[i]==31:
        print(i, end=' ')

print("")
l1=[]
for i in d:
    l1.append([d[i],[i]])
l1.sort()
l2=[]
for i in l1:
    l2.append([i[1], i[0]])

print("Months sorted by days:", l2)