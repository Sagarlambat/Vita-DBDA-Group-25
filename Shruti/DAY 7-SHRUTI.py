
#1.
class Bank:
       def __init__(self):
              self.balance=0
              print("Welcome....")

       def deposit(self):
               amount=float(input("Enter amount to be deposited...: ")) 
               self.balance += amount 
               print("\n Amount Deposited is:",amount) 
  
       def withdraw(self):
              amount = float(input("Enter amount to be withdrawn...: ")) 
              if self.balance>=amount:
                    self.balance-=amount
                    print("\n You have withdrawn...:", amount) 
              else:
                    print("\n You have insufficient balance...:  ") 
  
       def display(self):
              print("\n Net Available Balance:...",self.balance,  "\n EXIT")

x = Bank() 

x.deposit() 
x.withdraw() 
x.display() 


#2.
class Circle:
       def __init__(self,r):
              self.radius=r
       def area(self):
              return 14*self.radius*self.radius
       def perimeter(self):
              return 2*3.14*self.radius
c=Circle(5)
print("Area of circle...:",c.area())
print("Perimeter of circle...:",c.perimeter())

#3.
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
newSquare=Square(4)
print("Area of square is:",newSquare.area())

#4.
class MyClass:
       count_variable=0

       def __init__(self,a):
              self.number=a
              MyClass.count_variable+=1

m1=MyClass(5)
m2=MyClass(10)
m3=MyClass(20)
m4=MyClass(8)

print("Number of reference variables:",MyClass.count_variable)

#5.
class Salary:
    def __init__(self, pay):
        self.pay = pay
 
    def get_total(self):
        return (self.pay*12)
 
 
class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay)
 
    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() + self.bonus)
 
 
obj_emp = Employee(600, 500)
print(obj_emp.annual_salary())
 


