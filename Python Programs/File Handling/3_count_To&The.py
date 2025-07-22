with open("Poem.txt","r") as f:
    data=f.read()
    to_count=0
    the_count=0
    word=data.split()
    for i in word:
        if i.lower()=="to":
            to_count+=1
        elif i.lower()=="the":
            the_count+=1
print("Count of to: ",to_count)
print("Count of the: ",the_count)
            
        