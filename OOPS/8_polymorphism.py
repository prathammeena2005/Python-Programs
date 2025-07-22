class Animal:
    def speak(self):
        return self.speak

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

animal1=Dog()
animal2=Cat()
animal3=Duck()
print(animal1.speak())
print(animal2.speak())
print(animal3.speak())