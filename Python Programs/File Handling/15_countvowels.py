def count_vowels(file):
    with open(file,'r') as f:
        data=f.read()
        vowels="AEIOUaeiou"
        count=0
        for i in data:
            if i in vowels:
                count+=1
        return count
print("Number of vowels in file =  ",count_vowels('Poem.txt'))

