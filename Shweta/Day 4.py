'''
#Q1)write a function to find max of three numbers.
def max_number(a,b,c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    else:
        return c
print (max_number(10,200,50))
'''
'''
#Q2)write a python program to detect the number of local variables declared in a funtion.
def local_var():
    x,y,z=80,90,100
print(local_var.__code__.co_nlocals)
'''
'''
#Q3)Write a recursive function to calculate the sum of numbers from 0 to 10.
n=int(input("enter number: "))
def sum_of_nos(n):
    if n<=0:
        return n
    else:
        return n + sum_of_nos(n-1)
print(sum_of_nos(n))
'''
'''
#Q5)write a function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
    x= []
    for i in l:
        if i not in x:
            x.append(i)
    return x
print(unique_list([11,22,22,33,33,33,44,55,55,66]))
'''
'''
#Q6)Write a program to obtain the sum of the first and last digit of this number 2 user defined functions
#1st for first digit,2nd for last digit.
no=int(input("enter a number: "))
def first_digit(no):
    first=no
    while first>=10:
        first=first//10
    return first
def last_digit(no):
    last=no%10
    return last
print("sum of first and last digit is: ", first_digit(no)+last_digit(no))'''
