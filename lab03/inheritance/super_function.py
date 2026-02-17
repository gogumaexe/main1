# super_function.py
# Using super() to call parent class constructor

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def show(self):
        print(f"Name: {self.name}, Grade: {self.grade}")

student = Student("Alice", 10)
student.show()