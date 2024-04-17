class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.say_hello() # Output: "Hello, my name is Alice and I'm 25 years old."
person2.say_hello() # Output: "Hello, my name is Bob and I'm 30 years old."
