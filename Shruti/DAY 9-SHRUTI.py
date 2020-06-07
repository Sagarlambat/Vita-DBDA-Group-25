
#1.
def getException(num1,num2):
    try:
        x=num1/num2
        print('\nValue of',num1,'/',num2,'is -->',x)
    except Exception as e:
        print("\nCaught some exception of type",type(e).__name__)
    finally:
        print("Program Completed!!")
        
getException(5,2)
getException(5,0)

#2.
import re

def validatePhone(phone):
    if len(phone)==10 and re.findall('\d',phone):
        print('Valid Phone Number')
    else:
        print('Invalid Phone Number')

phone1=input("\nEnter Phone Number: ")
validatePhone(phone1)
phone2=input('\nEnter Phone Number: ')
validatePhone(phone2)

#3.
import re
def checkEmail(mail):
    if re.search('^\w+[@]+\S+[.]+\S{2,3}$',mail):
        print("Valid Mail ID")
    else:
        print('Invalid Mail ID')
        
mail=input("Enter Email: ")
checkEmail(mail)
mail=input("Enter Email: ")
checkEmail(mail)

#4.

import re
def checkCar(regNum):
    if re.search('^MH',regNum):
        print("Valid Maharashtra State Registration Number")
    else:
        print("Invalid Maharashtra State Registration Number")
        
regNum=input("Enter Email: ")
checkCar(regNum)
regNum=input("\nEnter Email: ")
checkCar(regNum)


#5.
def arith(a,b,o):
    if o=='+':
        print(a,'+',b,'=',a+b)
    elif o=='-':
        print(a,'-',b,'=',a-b)
    elif o=='*':
        print(a,'*',b,'=',a*b)
    elif o=='/':
        print(a,'/',b,'=',a/b)
        
def arithDecorator(func):
    def inner(a,b,o):
        if a<b:
            a,b=b,a
        return func(a,b,o)
    return inner

arith=arithDecorator(arith)
arith(4,8,'+')
arith(4,8,'-')
arith(4,8,'*')
arith(4,8,'/')

#6.
def fib():
    a,b=0,1
    for _ in range(100):
        yield a
        a,b=b,a+b         

f=fib()
a=list(f)
print(a)
