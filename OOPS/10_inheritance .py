class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

class Cat(Animal): # Cat inherits from Animal
    def meow(self):
        return f"{self.name} says Meow!"

my_cat = Cat("Whiskers")
print(my_cat.eat())  # Output: Whiskers is eating.
print(my_cat.meow()) # Output: Whiskers says Meow!