import random 
n=random.randint(1,100)
guesses=0
while True:
    guesses+=1
    a=int(input("Guess the number: "))
    if (a>n):
        print("Enter lower number...")
    elif (a<n):
        print("Enter higher number...")
    else:
        print(f"You have guessed the number {n} in {guesses} attempt.")
        break

print("----GAME OVER----")