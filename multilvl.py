# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating.")
        
# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} is barking.")
        
# Child class inheriting from Dog
class Labrador(Dog):
    def __init__(self, name):
        super().__init__(name, "Labrador")
        
    def swim(self):
        print(f"{self.name} is swimming.")
        
# Create instances of the classes
animal = Animal("Animal")
dog = Dog("Dog", "Labrador")
labrador = Labrador("Max")

# Call methods on the instances
animal.eat()  # Output: Animal is eating.
dog.eat()  # Output: Dog is eating.
dog.bark()  # Output: Dog is barking.
labrador.eat()  # Output: Max is eating.
labrador.bark()  # Output: Max is barking.
labrador.swim()  # Output: Max is swimming.
