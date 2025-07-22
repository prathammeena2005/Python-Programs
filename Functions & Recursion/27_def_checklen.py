word1=input("Enter a word: ")
word2=input("Enter a word: ")
def calc_len(w1,w2):
    if len(w1)==len(w2):
        print("Both strings have same length: True")
    else:
        print("Both strings donot have same length: False")
calc_len(word1,word2)