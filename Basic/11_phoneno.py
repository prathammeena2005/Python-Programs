phnum=input("Enter phone number (in XXX-XXX-XXXX formate): ")
if len(phnum)==12 and phnum[3]=='-' and phnum[7]=='-':
    if phnum[:3].isdigit() and phnum[4:7].isdigit() and phnum[8:].isdigit():
        print('Valid formate')
else:
    print('Invalid formate')       