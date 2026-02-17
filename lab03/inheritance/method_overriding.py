# method_overriding.py
# Method overriding example

class Bird:
    def fly(self):
        print("Bird is flying")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly, they swim!")

bird = Bird()
penguin = Penguin()

bird.fly()
penguin.fly()