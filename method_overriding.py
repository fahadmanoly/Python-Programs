class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")

# Create instances of the classes
animal = Animal()
dog = Dog()

# Call the speak method on each instance
animal.speak()  # Output: The animal makes a sound
dog.speak()  # Output: The dog barks
