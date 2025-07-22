import pickle
code=input("Enter staff code to search: ")
def search_staff(staffcode):
    try:
        with open("staff.dat","rb") as f:
            while True:
                data=pickle.load(f)
                if data['Staffcode']==staffcode:
                    print("Staff code= ",data['Staffcode'])
                    print("Staff name= ", data['Name'])
                    found=True
            
    except EOFError:
        if found==False:
            print("No data found!")
        else:
            print("Search successful!")
        f.close()
search_staff(code)