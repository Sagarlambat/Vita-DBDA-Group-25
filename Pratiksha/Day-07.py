#1.Write python program to perform bank operations using class and objects.
#Conditions:
#a.Bank name should be static.
#b.Using menu driven program.
#1 .Deposit
#2. Withdraw
#3. Exit
'''
class Bank:
    Name='Vita Bank'
    def __init__(self):
        self.Bal=0.00
    def Deposit(self):
        amount=float(input("Enter your amount"))
        self.Bal += amount
        print("your balance is:\n",self.Bal)

    def Withdraw(self):
        amount=int(input("Enter amount to withdraw\n"))
        if amount > self.Bal:
            raise ValueError("insufficient funds")
        self.Bal -= amount
        print("you have sucessfully withdraw amount Rs.\n",amount)
        print("your remaining balance is:\n",self.Bal)

    def Get_balance(self): 
        print("your balabce is\n",self.Bal)
b1=Bank()
loop=True
while loop==True:
    a=input("Welcome to Vita Bank\n Press for Deposit:1\nWithdraw:2\nGet_balance:3\n Exit:4\n")
    if a=='1':
        b1.Deposit()
    if a=='2':
        b1.Withdraw()
    if a=='3':
        b1.Get_balance()
    if a=='4':
        print("Exit")
        loop=False
'''
#2.Write a Python class named Circle constructed by a radius and two
#methods which will compute the area and the perimeter of a circle.
'''
from math import pi
class Circle:
    def init(self,radius):
        self.radius=radius
    def area(self):
        self.area=(2**self.radius)*pi
        print("Area of Circle:",self.area)
    def perimeter(self):
        self.perimeter=2*pi*self.radius
        print("perimeter of circle",self.perimeter)
c1=Circle()
c1.init(4)
c1.area()
c1.perimeter()
'''
#3. Define a class named Shape and its subclass Square.The Square class
#has an init function which takes a length as argument. Both classes have
#a area function which can print the area of the shape where Shape's area is 0 by default.
#Hints:
#To override a method in super class, we can define a method with the same name in
#the super class.
'''
class Shape:
    def area(self,s_area=0):
        self.s_area=s_area
        print("Area of shape is:",self.s_area)
class Square(Shape):
    def __init__(self,length=4):
        self.length=length
    def area(self):
        a=(self.length*self.length)
        print("Area of square is",a)
s=Square()
s.area()
'''

#4. Write a program to count how many reference variables in a program.
'''
import sys
class refer:
    pass
r1=refer()
r2=r1
r3=r2
print("the number of reference variable:",sys.getrefcount(r1))
'''

#5.Write any program to achieve composition in Python.
'''
class Book:
    def __init__(self,name):
        self.name=name
    def book_details(self):
        return self.name
class Chapter:
    def __init__(self,name,no):
        self.name=name
        self.no=no
        self.b=Book(self.name)
    def info(self):
        return "Book_Name "+ str(self.b.book_details())+"\n"+str(self.no)

c=Chapter("Python","Ch-10")
print(c.info())
'''







        
