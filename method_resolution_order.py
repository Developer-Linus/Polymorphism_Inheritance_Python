class A:
    def greet(self):
        print("Hello from class A.")
class B:
    def greet(self):
        print("Hello from class B.")
class C(A):
    def greet(self):
        print("Hello from class C.")
class D(B,C):
    pass

obj_d = D()
obj_d.greet()
'''
Let’s break it down:

Class D inherits from classes B and C, which in turn inherit from class A.
When we call obj_d.greet(), Python follows the MRO to determine which greet() method to execute.
The MRO for class D in this case is D -> B -> C -> A, following the depth-first left-to-right search.
Python finds the greet() method in class B first (left-most class in inheritance), so it executes the greet() method from class B.
Understanding MRO helps predict how Python resolves method calls in complex inheritance hierarchies. It ensures that methods are executed in the expected order, maintaining the integrity of your program’s logic even with multiple levels of inheritance.
'''