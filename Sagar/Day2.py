#1.Write a Python program that accepts a word from the user and reverse it.
#Note: Without using reverse function.

a=input("Enter a word: ")
print(a[::-1])


#2.Write a Python program to count the number of even and odd numbers from a series of numbers.
#Sample numbers :
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Output :
#Number of even numbers : 4
#Number of odd numbers : 5


numbers=input("Enter numbers seperated by space:\n").split()
e=0
o=0
for i in numbers:
    if int(i)%2==0:
        e+=1
    else:
        o+=1
print("Number of even numbers: ",e)
print("Number of odd numbers: ",o)




#3.Write a Python program to create the multiplication table (from 1 to 10) of a number. 

a=int(input("Enter a no.: "))
for i in range(1,11):
    print(a*i)


#4.Given the triangle of consecutive odd numbers
#       		                1
#	                  3                           5
#                7                      9                         11
#       13                15                          17                        19
#Above triangle is given Calculate Sum of row wise 
#Example we call function :- row_sum_odd_numbers(2)
#Result will be=3+5=8

def row_sum_odd_numbers(x):
    return x*x*x

print(row_sum_odd_numbers(int(input("Enter a number: "))))


#5.Write python program to print the pattern given below
#Note: Take input from user
#A
#B   B
#C  C  C
#D  D  D  D
#E  E  E  E  E

x=0
y=0
z=5 
for x in range(1, z + 1): 
        for y in range(z,z-x , -1): 
            print(chr(ord('A') - 1 + x), end = "  "); 
        print("");

#6. Python Program to Read a Number n And Print the Series
#   “1+2+…..+n= “
#          sample:
#          Case 1:
#	Enter a number: 4
#   1 + 2 + 3 + 4 = 10
#   Case 2:
#   Enter a number: 5
#   1 + 2 + 3 + 4 + 5 = 15

a=int(input("Enter a no.: "))
s=0
for i in range(1,a+1):
    s+=i
    if a==i:
        print(i,end='')
    else:
        print(i,end='+')
print("=",s,sep='')


#7.Write python program to print the pattern given below
#Note: Take input from user
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

x=0
y=0
z=5 
for x in range(1, z + 1): 
        for y in range(z,z-x , -1): 
            print(0 + x, end = "  "); 
        print("");


