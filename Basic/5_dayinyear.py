days=['Sunday', 'Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
daynum=int(input("Enter day number between 2 to 365: "))
day=input("Enter day name: ")
word=(daynum+7)%7+days.index(day)-1
if word>6:
    word=word-7
print(days[word])