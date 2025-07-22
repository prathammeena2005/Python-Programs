print("Enter 1 for Leap Year or 2 for Common Year")
year=int(input("Enter: "))
hour=24
min=60
sec=60
secin1day= hour*min*sec
if (year==1):
    totalsec=secin1day*366
    print("Total seconds in Leap year=", totalsec)
else:
    totalsec=secin1day*365
    print("Total seconds in Common year=", totalsec)