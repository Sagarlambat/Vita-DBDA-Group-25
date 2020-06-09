'''
#Q5)Write a python program to square and cube every number in a given list of integersbusing lambda.
no=[1,2,3,4,5]
print("Original list: ", no)
square_list=list(map(lambda s:s**2,no))
print("List of Squares: ",square_list)
cube_list=list(map(lambda s:s**3,no))
print("List of cubes: ",cube_list)'''

#Q1)Write a program to implement constructor with variable number of arguments.
def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)
multiply(6,5)

'''#Q3)write program to implement multiple inheritance
class s:
    def square(self):
        print('I am part of s')
class t :
    def triangle(self):
        print('I am part of t')
class r:
    def rectangle(self):
        print('I am part of r')
class h(s,t,r):
    def hexagon(self):
        print("I am part of h")
a=h()
a.square()
a.triangle()
a.rectangle()
a.hexagon()'''
'''
#Q4)write python program to implement operator overloading in python 
class Employee:
    def __init__(self,day1,day2):
        self.day1 = day1
        self.day2 = day2

    def __mul__(self,pay):
        day1=self.day1 * pay.day1
        day2=self.day2 * pay.day2
        e3=Employee(day1,day2)
        return e3

e1=Employee(28,30)
e2=Employee(500,500)
e3=e1*e2
print("First employees payment is: ",e3.day1)
print("Second employees payment is: ",e3.day2)'''

