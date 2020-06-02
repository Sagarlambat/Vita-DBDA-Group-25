#1.Write a program to implement Constructor with Variable Number of Arguments.
'''
class varargs:
    def __init__(self,*a):
        self.a=a
        print(a)
a=varargs(10,20,30,40,50)
'''
#3.Write a program to implement multiple inheritance.
'''
class a:
    def aim(self):
        print('I am in a')
class b:
    def bim(self):
        print('I am in b')
class c:
    def cim(self):
        print('I am in c')
class d(a,b,c):
    def dim(self):
        print("I am in d")
D=d()
D.aim()
D.bim()
D.cim()
D.dim()
'''
#5.	 Write a Python program to square and
#cube every number in a given list of integers using Lambda.
'''
a=[1,2,3,4,5,6,7]
s=list(map(lambda b:b**2,a))
c=list(map(lambda b:b**3,a))

for a,b,c in zip(a,list(map(lambda b:b**2,a)),list(map(lambda b:b**3,a))):
    print(a,b,c)

print(list(zip(a,s,c,)))
'''
#4.Write a program to implement operator overloading in python.
#overloading + operator
'''
class A:
    def __init__(self,a):
        self.a=a

    def __add__(self,o):
        return self.a*o.a

c=A(10)
d=A(20)
print(c+d)
'''
'''
# Python Program to perform addition 
# of two complex numbers using binary 
# + operator overloading. 
class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(self.a,self.b)
# adding two objects
    def __add__(self, other):
        print(other)
        return self.a + other.a, self.b + other.b 

    #def __str__(self):
        #return self.a,self.b

Ob1 = complex(1, 2) 
Ob2 = complex(2, 3)
Ob3=Ob1+Ob2
print(Ob3) 
'''
'''
# Python Program illustrate how 
# to overload an binary + operator 

class A:
    def __init__(self, a):
        self.a = a

# adding two objects
    def __add__(self, o):
        print(o.a)
        return self.a + o.a 
ob1 = A(1) 
ob2 = A(2)
ob5=A(100)
ob3 = A("Geeks") 
ob4 = A("For") 
print(ob1+ob5)
#print(ob1 + ob2) 
#print(ob3 + ob4) 
'''























