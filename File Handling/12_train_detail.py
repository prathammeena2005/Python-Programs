import pickle
num=int(input("Enter train no. to search: "))
def search_train(no):
    try:
        f=open("TRAIN.dat","rb")
        while True:
            data=pickle.load(f)
            if data['Trainno.']==no:
                print("Train no.= ",data['Trainno.'])
                print("From= ", data['From'])
                print("To= ", data['To'])
                found=True
    except EOFError:
        if found==False:
            print("No data found!")
        else:
            print("Search successful!")
        f.close()
search_train(num)