try:
    # Some code that may raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result of the division is: {result}")
    
except ValueError:
    print("Invalid input! Please enter a valid number.")
    
except ZeroDivisionError:
    print("Error! Cannot divide by zero.")
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    print("This code block will always run, regardless of whether an exception was raised or not.")
