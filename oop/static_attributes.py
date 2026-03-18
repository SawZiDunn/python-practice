# static attributes, also known as class attributes, are shared across all instances of a class.

class Dog:
    # Static attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Accessing static attribute
print(Dog.species)  # Output: Canis familiaris
# Creating instances of Dog
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris