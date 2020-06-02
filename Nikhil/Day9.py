#1.Write a function to compute divide by zero
#and use try/except to catch the exceptions.
'''
a=5
b=0
try:
    print(a//b)
except ZeroDivisionError:
    print('Error occured')
finally:
    print('Execution over')

'''
#2.Write python program to check  that given number
#is valid mobile number or not?
'''
import re
ip=input('Enter your mobile number')
a=re.fullmatch('[6789][0-9]{9}',ip)
if a!=None:
       print('Valid Mobile Number')
else:
    print('Invalid Mobile number')
'''   
#3.Write python program to check  that given email address is valid or not?
'''
import re
ip=input('Enter your email id')
a=re.fullmatch('\w[a-zA-Z0-9_.]*[@][a-z]*[.][a-z]*',ip)
if a!=None:
       print('Valid mail id')
else:
    print('Invalid Mail id')
'''
#4.	Write a python program to check given car registration number is
#valid Maharashtra state registration number or not?
'''
import re
ip=input('Enter your car number')
a=re.fullmatch('MH-[0][1-9]-[A-Za-z]{2}-[0-9]{4}',ip)
if a!=None:
       print('Valid car number')
else:
    print('Invalid car number')
'''
#5.Write a python program to decorate arithmetic operations.
'''
def my_decorator(function):
    def designer(a,b):
        print("Addition operation to be performed")
        function(a,b)
        print("Addition operation performed")

    return designer


@my_decorator
def add(a,b):
    print(a+b)
add(1,2)
'''
'''
def my_decorator(function):
    def designer(a,b):
        print("Subtraction operation to be performed")
        function(a,b)
        print("Subtraction operation performed")

    return designer


@my_decorator
def sub(a,b):
    print(a-b)
sub(1,2)
'''
#6.Write a python program to generate
#Fibonacci Numbers upto 100 using generator.
'''
def generator():
    a=0
    b=1
    for i in range(1001):
        yield a
        a,b=b,a+b
#for i in generator():
 #   print(i)
print(list(generator()))      
'''


















































