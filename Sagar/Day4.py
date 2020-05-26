#1.Write a function to find max of three numbers.

def maxofthree(x,y,z):
    if x>y and x>z:
        print(x)
    elif y>x and y>z:
        print(y)
    else:
        print(z)

x=int(input("Enter first no.: "))
y=int(input("Enter first no.: "))
z=int(input("Enter first no.: "))

maxofthree(x,y,z)    


#2.Write a Python program to detect the number of local variables declared in a function.

def detectnlocalvarialbles(n):
        return n.__code__.co_nlocals


def addition():
    x=10
    y=10
    print(x+y)

addition()    
print(detectnlocalvarialbles(addition))



#3.Write a recursive function to calculate the sum of numbers from 0 to 10
#Expected output: 56

def s10(a):
    if a<1:
        return 1
    else:
        return a+s10(a-1)

print(s10(10))



#4.Create a function showStudent() in such a way that it should accept student id, name, and it’s college name  and if the id and college name
#  is missing in function call it should show it as by default id is 1 and college name  is VITA.

def showStudent(name,id=1,college_name="VITA"):
            print(id,name,college_name)

showStudent("Sagar")
showStudent("Sagar",26,"RCOEM")

#5.Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [11,22,22,33,33,33,44,55,55,66]
#Unique List : [11, 22,33, 44, 55,66]

def uniquelist(a):
    return list(set(a))

a=input("Enter elements in list: ").split()
print("Sample List : ",a)
print("Unique List : ",sorted(uniquelist(a)))


#6.Write a program to obtain the sum of the first and last digit of this number 2 user defined functions
#1st for first digit
#2nd for last digit
#Example:
#Input:  5424
#Output: 9

n=int(input("Enter a number:"))
def first_digit(n):
       first=n
       while first>=10:
              first=first//10
       return first
def last_digit(n):
       last=n%10
       return last
print("Sum of first and last digits of no is:",first_digit(n)+last_digit(n))

