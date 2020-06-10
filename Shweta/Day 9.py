'''#Q1) write a function to compute divide by zero and use try/except to catch the exceptions.
def divide(a,b):
    try:
        ans=a//b
        print("Ans of division is: ",ans)
    except:
        print("Divide by zero")
divide(3,0)
divide(3,1)'''
'''
#Q2)write python program to check that given number is valid mobile number or not?
import re
no=input("Enter number: ")
n=re.compile("(0/91)?[7-9][0-9]{9}")
if(n.match(no)):
    print ("Valid mobile Number")      
else : 
    print ("Invalid mobile Number")'''

'''
#Q3)write python program to check that given email address is valid or not?    
import re
e=input("Enter email address: ")
x=re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
if(x.match(e)):
    print ("Valid E-mail id")      
else : 
    print ("Invalid E-mail id") '''

'''#Q4)write python program to check that given car registration number is valid Maharashtra state registration or not?
import re
no=input("Enter car registration number: ")
x=re.compile("^[MH]{2}[ -][0-9]{1,2}(?: [A-Z])?(?: [A-Z]*)? [0-9]{4}$")
if(x.match(no)):
    print ("Valid car registration number")      
else : 
    print ("Invalid car registration number")'''
    
#Q5)write a python program to decorate arithmetic operations.
def sub(x,y):
    print(x-y)

def sub1(func):
    def inner(x,y):
        if x<y:
            x,y=y,x
        return func(x,y)
    return inner
sub=sub1(sub)
sub(4,8)
'''
    
#Q6)write a python program to generate Fibonacci Numbers upto 100 using generator
def fibo():
    x=1
    y=1
    for i in range(101):
        yield x
        x,y=y,x+y
print(list(fibo()))'''


