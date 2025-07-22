import random
n = int(input("Enter the value of n:"))
def generate_number(n):
    lower_bound = 10 ** (n - 1)  
    upper_bound = (10 ** n) - 1   
    return random.randint(lower_bound, upper_bound)
random_number = generate_number(n)
print("Random number:", random_number)