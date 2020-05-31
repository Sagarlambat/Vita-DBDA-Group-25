#1.Write python program to perform bank operations using class and objects.
#  Conditions:
#a.Bank name should be static.
#b.Using menu driven program.
#1.Deposit
#2.Withdraw
#3.Exit
# Python program to create Bankaccount class 
# with both a deposit() and a withdraw() function 

class Bank:
    name='Python Bank'
    def __init__(self):
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
        s.balance_enquiry()
    if a=='4':
        print('Thank you')
        j=False 

#2. Write a Python class named Circle constructed by a radius and two
#   methods which will compute the area and the perimeter of a circle.

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
s=Circle()

s.init()
s.area()
s.perimeter()

#3. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have
#a area function which can print the area of the shape where Shape's area is 0 by default.
#Hints:
#To override a method in super class, we can define a method with the same name in the super class.

class Shape:
    def area(self,a=0):
        self.a=a
        print('Area of shape is:-',self.a)
    class square(Shape):
        def init(self,length):
            self.a=length**2
        def area(self):
            print('Area of square is:-',self.a)

#4. Write a program to count how many reference variables in a program.

import sys
class Demo:
    pass
a1=Demo()
a2=a1
a3=a2
a4=a3
print("The number of reference variable:",sys.getrefcount(a1))


#5. write any program to achieve composition in Python.

class Student:
    def __init__(self,no):
        self.no=no

    def no_of_student(self):
        return self.no
class Subject:
    def __init__(self,no,java,python):
        self.no=no
        self.java=java
        self.python=python
        self.student=Student(self.no)

    def info(self):
        return "Student" +str(self.student.no_of_student())+"\n"+str(self.java)+"\n"+str(self.python)

a=Subject(10,"OOPS","Panda")
print(a.info())

