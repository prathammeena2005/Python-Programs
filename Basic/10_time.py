time1=int(input("Enter first time: "))
time2=int(input("Enter second time: "))
diff=time2-time1
hour=diff//100
min=diff%100
print(diff)
print(hour,'hours',min,'minutes')