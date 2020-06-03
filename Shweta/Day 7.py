#Q1) write python program to perform bank operations using class and objects .
#conditions: a.Bank name should be static.
             #b. Using menu driven program.
                 #1. Deposite
                 #2. Withdraw
                 #3. Exit
class Bank:
    def __init__(self):
        self.balance=0
        print("Hello....")

    def deposite(self):
        amount=float(input('Enter amount to be deposited: '))
        self.balance+=amount
        print("\n Amount deposited: ",amount)

    def withdraw(self):
        amount=float(input('Enter amount to be withdrawn: '))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You withdraw: ",amount)
        else:
            print("\n Insufficient Balance")
        
    def display(self):
        print("\n Net Available Balance:....",self.balance, "\n EXIT")

a=Bank()
a.deposite()
a.withdraw()
a.display()

#Q2) Write a python class named Circle constructed by a radius and two methods which will compute the area
#and the perimeter of a circle.
class Circle:
    def __init__(self,r):
        self.radius=r
       
    def area(self):
        return 3.14*self.radius*self.radius
      
    def perimeter(self):
        return 2*3.14*self.radius

C=Circle(5)
print("Area: ",C.area())
print("Perimeter: ",C.perimeter())

#Q3)Define a class named Shape and its subclass Square. The Square class has an init function which  takes a length
#as argument. Both classes have a area function which can print the area of the shape where Shapes area is 0 by default.
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,l):
        Shape.__init__(self)
        self.length=l

    def area(self):
        return self.length*self.length

S=Square(6)
print("Area of square is: ", S.area())
     
#Q4) Write a program to count how many reference variables in a program.
class Count:
    count_var=0


    def __init__(self,c):
        self.number=c
        Count.count_var+=1

a1=Count(1)
a2=Count(2)
a3=Count(3)
a4=Count(4)

print("Number of reference variables is : ",Count.count_var)


#Q5) Write any program to achieve composition in python.
class Attendance:
    def __init__(self, total_days):
        self.total_days = total_days
        
    def get_total(self):
        return(self.total_days*1)
 
class Student:
    def __init__(self, total_days,present_days):
        self.total_days = total_days
        self.present_days = present_days
        self.obj_days = Attendance(self.total_days)
 
    def absent_days(self):
        return "Total: " + str(self.obj_days.get_total() - self.present_days)
 
 
obj_stu= Student(30,28)
print(obj_stu.absent_days())

