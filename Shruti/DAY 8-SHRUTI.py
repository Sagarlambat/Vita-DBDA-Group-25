
#1.
class fruits:
    def __init__(self,*args):
        print("Fruits Constructor with non keyword arguments\n",args)
        
class stud:
    def __init__(self,**kwargs):
        print('Stud constructor with keyword arguments\n',kwargs)
        
if __name__=='__main__':
    fruits('orange','mango','banana','pineapple')
    stud(sid=1,name='shruti',age=24,course='pg-dbda')

#3.
class A:
    def __init__(self):
        super().__init__()
        self.name='ABC'
        
    def getName(self):
        return self.name
        
class B:
    def __init__(self):
        super().__init__()
        self.name='XYZ'
        
    def getName(self):
        return self.name
        
class C(B,A):
    def __init__(self):
        super().__init__()
    def getName(self):
        return self.name
    
c=C()
print(c.getName())

#4.
class marks:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def __add__(self,other):
        a=self.a+other.a
        b=self.b+other.b
        #c=a+b
        return a,b

if __name__=='__main__':
    m=marks(10,15)
    m1=marks(20,25)
    print(marks.__add__(m,m1))

#5.
sqr=lambda n:n**2
cube=lambda n:n**3
print(sqr(int(input("Enter Number to find Square: "))))
print(cube(int(input("Enter Number to find Cube: "))))

