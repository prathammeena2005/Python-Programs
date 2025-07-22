import pickle
def cpy_records(file1,file2):
    try:
        f1=open(file1,"rb")
        f2=open(file2,"wb")
        i=0
        while True:
            data=pickle.load(f1)
            
            word=data.split('-')
            
            for i in word:
                
                if i=='Atheletics':
                    print(i)
                    
                    pickle.dump(data,f2)
                    
    except EOFError:
        f1.close()
        f2.close()
cpy_records("sports.dat","Atheletics.dat")   

        