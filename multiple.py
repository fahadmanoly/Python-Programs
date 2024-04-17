# Parent class 1
class A:
    def method_a(self):
        print("Method A")
        
# Parent class 2
class B:
    def method_a(self):
        print("Method B")
        
# Child class inheriting from A and B
class C(A, B):
    def method_c(self):
        print("Method C")
        
# Create an instance of the class
c = C()

# Call methods on the instance
c.method_a()  # Output: Method A
#c.method_b()  # Output: Method B
c.method_c()  # Output: Method C
