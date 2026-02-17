# class_variables.py
# Class vs instance variables

class Dog:
    species = "Canine"  # class variable

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Max", "Bulldog")
dog2 = Dog("Rocky", "Labrador")

print(dog1.species)
dog1.species = "Wolf"  # modifies only for dog1

print(dog1.species)  # Wolf
print(dog2.species)  # Canine