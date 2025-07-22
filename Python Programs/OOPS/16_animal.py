class Animal:
    pass

class Pet(Animal):
    pass

class Dog(Pet):
    @staticmethod
    def bark():
        print("Woof! Woof!")

d=Dog()
d.bark()