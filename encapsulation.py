class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
            
    def get_balance(self):
        return self.__balance

# Create an instance of the BankAccount class
account = BankAccount("1234567890", 1000)

# Try to access the private properties of the object directly
# print(account.__account_number)  # Output: AttributeError: 'BankAccount' object has no attribute '__account_number'
# print(account.__balance)  # Output: AttributeError: 'BankAccount' object has no attribute '__balance'

# Call the public methods to interact with the object
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300

