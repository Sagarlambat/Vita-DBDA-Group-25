#Que 1:
#	Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#	between 2000 and 3200 (both included).
#	The numbers obtained should be printed in a comma-separated sequence on a single line.
#	
#	Hints: 
#
#             Consider use range(#begin, #end) method


'''
l=[]
for i in range(2000,3200):
       if i%7==0 and i%5!=0:
              l.append(i)
print(l)
'''



#Que2:
#	With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1
#       and n (both included). and then the program should print the dictionary.
#	Suppose the following input is supplied to the program:
#	8
#	Then, the output should be:
#	{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#	
#	Hints:
#	In case of input data being supplied to the question, it should be assumed to be a console input.
#	Consider use dict()

'''
a=dict()
c=int(input("Enter the value of n:"))
for i in range(1,c+1):
        a[i]=i*i
print(a)
'''


#Question3
#	Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#	Suppose the following input is supplied to the program:
#	Hello world
#	Practice makes perfect
#	Then, the output should be:
#	HELLO WORLD
#	PRACTICE MAKES PERFECT
#	
#	Hints:
#	In case of input data being supplied to the question, it should be assumed to be a console input.

'''
l=[]
while True:
        x=input("Enter sequence of lines:")
        if x:
                l.append(x)
        else:
                break
for s in l:
        print(s.upper())
'''

#Question 4:
#
#Write a program to check wheather number is even or odd using if 
#Else statement…

'''
x=int(input("Enter value of n:"))
if (x%2==0):
      print("no. is even",x)
else:
       print("no. is odd:",x)

'''



#Question 5:
#
#program that grants access only to kids aged between 8-12
#using  if  else statement
#Hint::
#If aged between 8 to 12 then you are allowed… welcome!!
#Otherwise Sorry not allowed ..Bye!
'''
x=int(input("Enter age:"))
if x>=8 and x<=12:
       print("you are allowed… welcome!!")
else:
       print("Sorry not allowed ..Bye!")
'''
