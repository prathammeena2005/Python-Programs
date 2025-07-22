l=eval(input("Enter a list: "))
longest=''
word=0
for i in l:
    if len(i)>word:
        word=len(i)
        longest=i
print("Longest word in list=", longest)