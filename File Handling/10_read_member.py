import pickle
try:
    f=open ("member.dat", "rb")
    while True:
        print(pickle.load(f))
except EOFError:
    f.close()