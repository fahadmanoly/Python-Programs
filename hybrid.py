# Parent class 1
class A:
    def method_a(self):
        print("Method A")
        
# Parent class 2
class B:
    def method_b(self):
        print("Method B")
        
# Child class inheriting from A and B
class C(A, B):
    def method_c(self):
        print("Method C")
        
# Child class inheriting from B
class D(B):
    def method_d(self):
        print("Method D")
        
# Child class inheriting from C and D
class E(C, D):
    def method_e(self):
        print("Method E")
        
# Create an instance of the class
e = E()

# Call methods on the instance
e.method_a()  # Output: Method A
e.method_b()  # Output: Method B
e.method_c()  # Output: Method C
e.method_d()  # Output: Method D
e.method_e()  # Output: Method E
