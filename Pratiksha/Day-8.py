#1.Write a program to implement Constructor with Variable Number of Arguments.
'''
class Demo:
    def __init__(self,Name='XYZ',Gender='Female'):
        self.Name=Name
        self.Gender=Gender
d1=Demo()
print("Name is:",d1.Name,"Gender is:",d1.Gender)
'''
#2.Write a program to implement Constructor Overloading.
'''
class A:
    def __init__(self):
        self.Name="Pratiksha"
    
class B(A):
    def __init__(self):
        self.Name="VITA"
    def display(self):
        print(self.Name)
a=B()
a.display()
'''
#3.Write a program to implement multiple inheritance.
'''
class Base1:
    def __init__(self):
        self.Name="Pratiksha"
        print("Base1")
class Base2:
    def __init__(self):
        self.address="Ghatkoper"
        print("Base2")
class Derived(Base1,Base2):
    def __init__(self):
        Base1. __init__(self)
        Base2.__init__(self)
        print("Derived")
        print(self.Name,self.address)
d=Derived()
'''
#4.Write a program to implement operator overloading in python.
'''
class Demo:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b.a
    def __mul__(self,c):
        return self.a*c.a
d1=Demo(5)
d2=Demo(8)
d5=Demo(2)
d3=Demo('Operator ')
d4=Demo('Overloading')
print(d1+d2)
print(d3+d4)
print(d1*d5)
'''
#5.Write a Python program to square and cube every number in a given list of integers using Lambda.
'''
list1=[1,2,3,4,5,6,7,8,9,10]
print("Original lsit of integers:\n",list1)
square=list(map(lambda x:x**2,list1))
print("Square of every number in list:\n",square)
cube=list(map(lambda x:x**3,list1))
print("Cube of every number in list:\n",cube)
'''







