#1.Write a function to compute divide by zero and use try/except to catch the exceptions.


def reciprocal(x):

    try:
        print("The reciprocal of",x,"is",1/x)
    except ZeroDivisionError:
        print("Oops! ZeroDivisionError occured.")
        
x=int(input("Enter you no.: "))
reciprocal(x) 


#2.Write python program to check  that given number is valid mobile number or not?


import re
s=input("Enter number: ")
a=re.compile("(0/91)?[7-9][0-9]{9}")
if(a.match(s)):
    print ("Valid Number")      
else : 
    print ("Invalid Number") 


#3.Write python program to check  that given email address is valid or not?


import re
s=input("Enter email address: ")
a=re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
if(a.match(s)):
    print ("Valid E-mail id")      
else : 
    print ("Invalid E-mail id") 


#4.Write a python program to check given car registration number is valid Maharashtra state registration number or not?


import re
s=input("Enter car registration number: ")
a=re.compile("^[MH]{2}[ -][0-9]{1,2}(?: [A-Z])?(?: [A-Z]*)? [0-9]{4}$")
if(a.match(s)):
    print ("Valid car registration number")      
else : 
    print ("Invalid car registration number")


#5.Write a python program to decorate arithmetic operations.

def decorator(f1):
    def operation():
        print("operation starts")
        f1()
        print("operation finshed")
    return operation

@decorator
def mul():
    a=int(input("Enter 1st no: "))
    b=int(input("Enter 2nd no: "))
    print("Multiplication of",a,"&",b,"is",a*b)


#6.Write a python program to generate Fibonacci Numbers upto 100 using generator.


def fibo(x):
    a=1
    b=1
    for i in range(x):
        yield a
        a,b = b,a+b

for i in fibo(100):
    print(i)
