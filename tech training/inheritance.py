# single level inheritance
"""class Vehicle:
    def __init__(self,b,p,c,s):      # brand,price,color,seating size
        self.b=b
        self.p=p
        self.c=c
        self.s=s
        print("Vehicle class constructor")
class Bike(Vehicle):
    def __init__(self, b, p, c, s,g,m):  # gear,milage
        super().__init__(b, p, c, s)
        self.g=g
        self.m=m
        print("Bike class constructor")
b1=Bike('Tata',25000,'Black',2,3,45)"""

# multi level inheritance
"""class Grandparent:
    def trait1(self):
        print("Grandparent trait")

class Parent(Grandparent):  # Parent inherits from Grandparent
    def trait2(self):
        print("Parent trait")

class Child(Parent):  # Child inherits from Parent
    def trait3(self):
        print("Child trait")

c = Child()
c.trait1()  # from Grandparent
c.trait2()  # from Parent  
c.trait3()  # from Child"""

# multiple inheritance
"""class Father:
    def s1(self):
        print("Father: Siva")

class Mother:
    def s2(self): 
        print("Mother: Sunitha")

class Child(Father, Mother):  # inherits from both
    def s3(self): 
        print("Child: Renuka")

c = Child()
c.s1() 
c.s2()
c.s3()"""

# hierarchical inheritance
"""class Parent:
    def family(self): 
        print("Siva")

class Son(Parent):  # both inherit from Parent
    def hobby(self): 
        print("Son likes cricket")

class Daughter(Parent):
    def hobby(self): 
        print("Daughter likes singing")

s = Son(); 
d = Daughter()
s.family()
s.hobby()
d.family()
d.hobby()"""

# hybrid inheritance
class A:
    def m1(self): 
        print("A")
class B(A): 
    pass  # multi-level
class C(A): 
    pass  # hierarchical
class D(B, C): 
    pass  # multiple + multi-level = hybrid
d = D()
d.m1()

