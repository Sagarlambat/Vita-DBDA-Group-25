#1.Write a function to find max of three numbers.
'''
def max_no(no1,no2,no3):
    if((no1>no2)&(no1>no3)):
        return no1
    elif((no2>no1)&(no2>no3)):
        return no2
    else:
        return no3
no1=int(input("Enter the no1"))
no2=int(input("Enter the no2"))
no3=int(input("Enter the no3"))
res=max_no(no1,no2,no3)
print("Maximum no is:",res)
'''
#2.Write a Python program to detect the number of local variables declared in a function.
'''
def sample():
    a=0
    s=' '
    b=0
print("Number of local variables are:")
print(sample.__code__.co_nlocals)
'''
#3.Write a recursive function to calculate the sum of numbers from 0 to 10
#Expected output: 55
'''
def recursive_sum(no):
    if no<=1:
        return no
    return no + recursive_sum(no-1)
no=int(input("Enter of no"))
print("sum of numbers:")
print(recursive_sum(no))
'''
#4.Create a function showStudent() in such a way that it should accept student
#id, name, and it’s college name  and if the id and college name is missing in
#function call it should show it as by default id is 1 and college name  is VITA.
'''
def showStudent(S_Name,S_id=1,college_Name='VITA'):
    print("Student id is:",S_id,"\nName of student:",S_Name,"\ncollege_Name:",college_Name)

showStudent("Pratiksha",25,"JSPM")
showStudent("XYZ")
'''
#5.Write a Python function that takes a list and returns a new list with unique elements of the first list.
'''
def unique_Element(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2
print(unique_Element([4,2,5,6,4,2,6,8]))
    
'''
#6.Write a program to obtain the sum of the first and last digit of this number 2 user defined functions
#1st for first digit
#2nd for last digit
'''
def first_digit(no):
    while no>=10:
        no=no/10
    return int(no)
def last_digit(no):
    return no%10
no=int(input("enter the no"))
print(first_digit(no),last_digit(no))
sum_is=first_digit(no)+last_digit(no)
print("Sum of first and last digit:",sum_is)
'''





