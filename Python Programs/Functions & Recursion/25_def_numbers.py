num=int(input("Enter a number: "))
def calc_cube(n=2):
    a=n**3
    print("Cube of", num, "=", a)
calc_cube(num)

word1=input("Enter a word: ")
word2=input("Enter a word: ")
def calc_len(w1,w2):
    if len(w1)==len(w2):
        print(True)
    else:
        print(False)
calc_len(word1,word2)