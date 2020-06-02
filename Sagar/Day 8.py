#1.Write a program to implement Constructor with Variable Number of Arguments.
'''
class Human:

    def __init__(self,*x):
        self.x=x
        print(self.x)

y=Human("Sagar","Python","DBDA","Nikhil","Pritam",1,2,3,4,5)
'''

#2.Write a program to implement Constructor Overloading.
'''
class Human:

    def __init__(self,name="XYZ",age=0,gender):
        self.name=name
        self.age=age
        print(self.name,self.age)

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("Second")
        print(self.name,self.age,self.gender)

#s=Human("Yash",50,"fdsa")

y=Human("Sagar",50,"Male")
'''
#3.Write a program to implement multiple inheritance.
'''
class a:
    def aim(self):
        print("I am in a")

class b:
    def bim(self):
        print("I am in b")

class c:
    def cim(self):
        print("I am in c")

class d(a,b,c):
'''
#4.Write a program to implement operator overloading in python.
'''
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1 + other.m1
        m2=self.m2 + other.m2
        return m1,m2

s1 = Student(1,2)
s2 = Student(5,6)
s3 = s1 + s2
print(s3)
'''
#5.Write a Python program to square and cube every number in a given list of integers using Lambda.
'''
a=[1,2,3,4,5,6]
print(list(map(lambda s: s**2,a)))
print(list(map(lambda s: s**3,a)))

for a,b,c in zip(a,list(map(lambda s: s**2,a)),list(map(lambda s: s**3,a))):
    print(a,b,c)


    def dim(self):
        print("I am in d")
x=d()
x.aim()
x.bim()
x.cim()
x.dim()
'''
