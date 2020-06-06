#1.Write a function to compute divide by zero and use try/except to catch the exceptions.
'''
list1=[0,0,2]
for i in list1:
    try:
        print(i)
        res=1/i
        break
    except Exception as e:
        print("Exception Occurred",e)
        print("Next Entry")
print("The reciprocal of",i,"is",res)
'''
#2.Write python program to check  that given number is valid mobile number or not?''
'''
import re
no=input("Enter phn number")
a=re.compile("(0/91)?[7-9][0-9]{9}")

if(a.match(no)):
    print("Phone no is valid")
else:
    print("Phone no is not valid")
'''
#3.Write python program to check  that given email address is valid or not?
'''
import re
def EmailValid(email):
    x=re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
    return x.match(email)
email=input("Enter Email address:")
if(EmailValid(email)):
    print("Email address is valid")
else:
    print("Incorrect Email address")
'''
#4.Write a python program to check given car registration number is valid Maharashtra state registration number or not?
'''
import re
def regno(no):
    x=re.compile("^[MH]{2}[ -][0-9]{1,2}(?:[A-Z]?(?:[A-Z]*)?[0-9]{4}$")
    return x.match(no)
no=input("Enter the no:")
if(regno(no)):
    print("Car registration no is valid for maharashtra state")
else:
    print("Registration no is invalid")
'''
#5.Write a python program to decorate arithmetic operations.
'''
def decorator(function):
    def designer(no1,no2):
        print("Addition performed")
        function(no1,no2)
    return designer
@decorator
def add(no1,no2):
    print(no1+no2)
add(8,5)
'''
#6.Write a python program to generate Fibonacci Numbers upto 100 using generator.
'''
def fibo():
    x=0
    y=1
    for i in range(101):
        yield x
        x,y=y,x+y
print(list(fibo()))
'''













