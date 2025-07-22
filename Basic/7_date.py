month={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August', '09':'September','10':'October','11':'November','12':'December'}
date=input("Enter date (in MMDDYYYY formate): ")

a=date[0:2]
b=month[a]
c=date[2:4]
d=date[4:]
print(b,c,d)