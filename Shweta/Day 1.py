'''
#Q1)write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#(between 2000 and 3200 included). The numbers obtained should be printed in comma-seperated sequence on a single line.
l=[]
for i in range(2000,3201):
    if i%7==0:
        if i%5!=0:
            l.append(i)
print(l)
'''
'''
#Q2)With a given integral number n, write a program to generate a dictionary that contains (i,i*i)such that is an intergral
#number between 1 and n(both included). and then the program should print the dictionary.
dict={}
n=int(input("enter a number: "))
for i in range(1,n+1):
    dict[i]=i*i
print(dict)
'''

'''
#Q3)
list=[]
while True:
    l=input("enter lines: ")
    if l:
        list.append(l)
    else:
        break
for s in list:
    print(s.upper())   
'''
'''
#Q4)write a program to check wheather number is even or odd using if else statement...
num=int(input("enter a number: "))
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")
'''
'''
#Q5)Program that grants access only to kids aged between 8-12 using if else statement.
#Hint:if aged between 8 to 12 then you are allowed... welcome!! otherwise Sorry not allowed..Bye!
age=int(input("enter age of kid:"))
if (8<=age<13):
    print("You are allowed... Welcome!!")
else:
    print("Sorry not allowed.. Bye!")
'''
