with open("Article.txt") as f:
    data=f.read()
    count=0
    for i in data:
        if i.isupper():
            count+=1
print("Number of upper-case alphabets in file = ",count)