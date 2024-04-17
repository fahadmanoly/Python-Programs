class Animal:
    def __init__(self, name):
        self.name = name
        
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

# Create instances of the classes
dog = Dog("Rufus")
cat = Cat("Whiskers")
bird = Bird("Tweety")

# Call the make_sound method on each instance
print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
print(bird.make_sound())  # Output: Chirp!
