#1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
'''
for no in range(2000,3200):
    if((no%7==0)&(no%5!=0)):
        print(no)
'''
#2.With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
#such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
#solution 1
'''
def squ(no):
    square={}
    for i in range(1,no+1):
        square[i]=i*i
    return square
no=int(input("Enter no"))
print(squ(no))
'''
#solution 2
'''
no=int(input("Enter the no"))
square={i:i*i for i in range(1,no+1)}
print(square)
'''

#3.Write a program that accepts sequence of lines as input and prints the lines
#after making all characters in the sentence capitalized.

'''
line=[]
while True:
    ch=input("Enter sequence of lines:\nType 'quit' to 'exit'")
    if ch=='quit':
        break
    else:
        line.append(ch)
for sen in line:
    print(sen.upper())
'''
#4.Write a program to check wheather number is even or odd using if 
#Else statement…
'''
no=int(input("Enter the no"))
if no%2==0:
    print("Number is even")
else:
    print("Number is odd")
'''

#5.program that grants access only to kids aged between 8-12
#using  if  else statement

age=int(input("Enter the age of kid"))
if ((age>=8) & (age<=12)):
    print("You are allowed....Welcome!")
else:
    print("Sorry you are not allowed...Bye!")

