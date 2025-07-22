import random
import string
allcharacters= string.ascii_letters + string.digits + string.punctuation
pass_len=int(input("Enter length of password: "))
password=""
if (pass_len>=8):
    for i in range(pass_len):
        password+= random.choice(allcharacters)
    print("Your random password is:", password)
else:
    print("Password length must be greater of equal to 8.")
