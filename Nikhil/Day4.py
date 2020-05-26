#1.Write a function to find max of three numbers.
'''
def max3(nolist):
    print(max(nolist))
a=list(map(int,input("Enter three numbers").split()))
max3(a)
'''
#2.	Write a Python program to detect the number
#of local variables declared in a function.
#We can use the co_nlocals() function which returns the number of local
#variables used by the function to get the desired result.
'''
def fun():
    a,b,c,d=1,2,3,4

print(fun.__code__.co_nlocals)
'''
#3.Write a recursive function to calculate the sum of numbers from 0 to 10
#Expected output: 55
'''
def sum10(a):
    if a<=1:
        return 1
    else:
        return a+sum10(a-1)
print(sum10(10))
'''
#4.Create a function showStudent() in
#such a way that it should accept student id,
#name, and it’s college name  and if the id and
#college name is missing in function call it should
#show it as by default id is 1 and college name  is VITA.
'''
def showstudent(name,id=1,cname='vita'):
    print('college id=',id,'\nStudentname=',name,'\ncollegename=',cname)

showstudent('nikhil')
'''
#5.Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [11,22,22,33,33,33,44,55,55,66]
#Unique List : [11, 22,33, 44, 55,66]
'''
Sample_List=[11,22,22,33,33,33,44,55,55,66]
print(list(set(Sample_List)))
'''
#6.Write a program to obtain the sum of the
#first and last digit of this number 2 user defined functions
#1st for first digit
#2nd for last digit
#Example:
# Input:  5424
#Output: 9
'''
def afl(no):
    no=list(str(no))
    return int(no[0])+int(no[len(no)-1])
print(afl(5424))
'''
