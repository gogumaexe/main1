# multiple_inheritance.py
# Demonstrating multiple inheritance

class Engine:
    def start(self):
        print("Engine started")

class Wheels:
    def rotate(self):
        print("Wheels rotating")

class Car(Engine, Wheels):
    def drive(self):
        print("Car is moving forward")

car = Car()
car.start()
car.rotate()
car.drive()