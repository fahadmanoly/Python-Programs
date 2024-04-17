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
        
# Child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
    def meow(self):
        print(f"{self.name} is meowing.")
        
# Create instances of the classes
animal = Animal("Animal")
dog = Dog("Dog", "Labrador")
cat = Cat("Cat", "Persian")

# Call methods on the instances
animal.eat()  # Output: Animal is eating.
dog.eat()  # Output: Dog is eating.
dog.bark()  # Output: Dog is barking.
cat.eat()  # Output: Cat is eating.
cat.meow()  # Output: Cat is meowing.
