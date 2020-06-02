#1.	Write python program to perform bank operations using class and objects.
 #      Conditions:
#a.	Bank name should be static.
#b.	Using menu driven program.
#1 .Deposit
#2. Withdraw
#3. Exit

'''
class Bank:
    name='Mybank'
    def init(self):
        self.balance=0
    def deposit(self):
        amount=float(input('Enter your amount\n'))
        self.balance+=amount
        print('your balance is\n',self.balance)
    def withdraw(self):
        amount=float(input('Enter amount to withdraw\n'))
        if self.balance>amount:
            self.balance-=amount
            print('You have sucessfully withrawn amount Rs:-\n',amount)
            print('your balance is\n',self.balance)
        else:
            print('Insufficient balance\n')
    def balance_enquiry(self):
        print('your balance is \n',self.balance)
s=Bank()
j=True
while j==True:
    a=input('Welcome to mybank \npress 1,2,3 for:-Deposit:1\nWithdrawl:-2\nBalance enquiry:3 quit:-4\n')
    if a=='1':
        s.deposit()
    if a=='2':
        s.withdraw()
    if a=='3':
        s.balance_enqiury()
    if a=='4':
        print('Thank you')
        j=False
'''

#2. Write a Python class named Circle constructed by a radius and two
#methods which will compute the area and the perimeter of a circle.
'''
from math import pi
class Circle:
    def init(self):
        radius=float(input('Enter the Radius'))
        self.radius=radius
    def area(self):
        self.area=pi*(self.radius**2)
        print('Area of circle:-',self.area)
    def perimeter(self):
        self.perimeter=2*pi*self.radius
        print('Perimeter of circle:-',self.perimeter)
'''
#3.Define a class named Shape and its subclass Square.
#The Square class has an init function which takes a
#length as argument. Both classes have a area function
#which can print the area of the shape where Shape's area is 0 by default.

#Hints:

#To override a method in super class, we can define a
#method with the same name in the super class.
'''
class Shape:
    def area(self,a=0):
        self.a=a
        print('Area of shape is:-',self.a)
class Square(Shape):
    def __init__(self,length):
        self.a=length**2
    def area(self):
        print('Area of square is:-',self.a)
a=Square(5)
a.area()
'''
#4.Write a program to count how many reference variables in a program. 
'''
import sys
class Demo:
    pass
d1=Demo()
d2=d1
d3=d2
d4=d3
print("The number of reference variable:",sys.getrefcount(d1))
'''
#5.write any program to achieve composition in Python.
'''
class Solders:
    def __init__(self,no):
        self.no=no
    def no_of_solders(self):
        return self.no
class Mission:
    def __init__(self,guns,magazines,no):
        self.no=no
        self.guns=guns
        self.magazines=magazines
        self.solders=Solders(self.no)
    def requirement(self):
        return 'The mission requires '+str(self.solders.no_of_solders())+' solders '+str(self.guns)+' guns '+str(self.magazines)+' magazines'

a=Mission(10,50,5)
print(a.requirement())
'''
        





































