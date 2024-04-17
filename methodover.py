class Calculator:
    def add(self, a, b=None, c=None):
        if b is None and c is None:
            return a
        elif c is None:
            return a + b
        else:
            return a + b + c
        
# Create an instance of the Calculator class
calculator = Calculator()

# Call the add method with one, two, and three arguments
print(calculator.add(1))  # Output: 1
print(calculator.add(1, 2))  # Output: 3
print(calculator.add(1, 2, 3))  # Output: 6
