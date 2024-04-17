from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2

# Create instances of the Rectangle and Circle classes
rectangle = Rectangle(5, 10)
circle = Circle(7)

# Call the area method on each instance
print(rectangle.area())  # Output: 50
print(circle.area())  # Output: 153.86
