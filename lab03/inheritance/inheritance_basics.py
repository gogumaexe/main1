# inheritance_basics.py
# Simple inheritance example

class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.speak()
dog.bark()