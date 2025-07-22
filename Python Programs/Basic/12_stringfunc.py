s=input("Enter sentence: ")
print("Original sentence", s)
count=1
alcount=0
for i in s:
    if i==' ':
        count+=1
    else:
        alcount+=1
prcnt=alcount/(len(s))*100
print("Number of words=", count)
print("Number of characters=", len(s))
print("Percentage of alpha numeric character=", prcnt)