# class_methods.py
# Demonstrates instance and class methods

class Student:
    school_name = "Greenwood High"  # class variable

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_info(self):
        print(f"{self.name} studies in grade {self.grade}")

    @classmethod
    def school(cls):
        print(f"School name: {cls.school_name}")

s1 = Student("Alice", 10)
s1.show_info()
Student.school()