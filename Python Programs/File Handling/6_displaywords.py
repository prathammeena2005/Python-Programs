def DISPLAYWORDS(file):
    with open(file,'r') as f:
        data=f.read()
        words=data.split()
        print("Words with less than 4 characters are: ")
        for i in words:
            if len(i)<4:
                print(i)
DISPLAYWORDS("Story.txt")