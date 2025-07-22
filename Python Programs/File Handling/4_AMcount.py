def AMCount(file):
    a_count=0
    m_count=0
    with open(file,"r") as f:
        data=f.read()
        for i in data:
            if i.lower()=='a':
                a_count+=1
            elif i.lower()=='m':
                m_count+=1
    print("Count of A or a: ",a_count)
    print("Count of M or m: ",m_count)
AMCount("Story.txt")