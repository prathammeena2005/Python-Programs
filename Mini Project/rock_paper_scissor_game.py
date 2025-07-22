import random
''' 
1 for Rock
2 for Paper
3 for Scissor
'''
option=[1,2,3]
computer=random.choice(option)
user=int(input('Enter (1 for Rock\n2 for Paper\n3 for Scissor): '))
print("You choose", user, "and Computer choose",computer)
if computer==user:
    print("It's a draw!")
else:
    if computer==1 and user==2:
        print("You win!")
    elif computer==1 and user==3:
        print("You lose!")
    elif computer==2 and user==1:
        print("You lose!")
    elif computer==2 and user==3:
        print("You win!")
    elif computer==3 and user==1:
        print("You win!")
    elif computer==3 and user==2:
        print("You lose!")
