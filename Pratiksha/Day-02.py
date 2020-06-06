#1.Python Program to Read a Number n And Print the Series “1+2+…..+n= “
#sol 1
'''
sum=0
n=int(input("enter no"))
for i in range(1,n+1):
    print(i,"+",end=" ")
    sum+=i
print("sum is=",sum)
'''
#sol 2
'''
no=int(input("Enter the no"))
s=[]
for i in range(1,no+1):
    print(i,end=" ")
    if(i<no):
        print("+",end=" ")
    s.append(i)
print("=",sum(s))
'''
#2. Write a Python program to count the number of even and odd numbers from a series of numbers.
'''
series=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for i in series:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("count of even no",even)
print("count of odd",odd)
'''
#3.Write a Python program to create the multiplication table (from 1 to 10) of a number.
'''
mul=0
no=int(input("Enter the no"))
for i in range(1,11):
    mul=no*i
    print(mul)
'''

# 4.Given the triangle of consecutive odd  numbers.

#row 1            1
#row 2        3       5
#row 3      7     9     11
#row 4    13  15   17    19
#row 5  21   23  25   27    29
#Above triangle is given Calculate Sum row wise 
#Example we call function :- row_sum_odd_numbers(2)
#Result will be=3 + 5 = 8
#if user give 4 then ur output is 13 + 15 + 17+ 19 = 64
'''
def row_sum_odd_numbers(no):
    return no*no*no
no=int(input("Enter no:"))
print(row_sum_odd_numbers(no))
'''
#5.Write python program to print the pattern given below.

n=int(input("Enter the no"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print("\n")

