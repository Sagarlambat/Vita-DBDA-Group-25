'''
1.	Python Program to Read a Number n And Print the Series “1+2+…..+n= “
          sample:
          Case 1:
	Enter a number: 4
1 + 2 + 3 + 4 = 10 
Case 2:
Enter a number: 5
1 + 2 + 3 + 4 + 5 = 15
'''
'''
no=int(input('Enter a number'))
sum=0
for i in range(1,no+1):
    if i==no:
        sum=sum+i
        print(i,end='')
    else:
      sum=sum+i
      print(i,end='+')
print('=',sum)
'''
'''
2. Write a Python program to count the number of even and odd numbers from                     a series of numbers.
Sample numbers :
 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Output :
Number of even numbers : 4
Number of odd numbers : 5
'''
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even=0
odd=0
for i in numbers:
    if i%2==0:
        even+=1
    else:
        odd+=1
print('Number of even numbers :',even,'\nNumber of odd numbers :',odd)

'''
'''
3.Write a Python program to create the
multiplication table (from 1 to 10) of a number. 
'''
'''
no=int(input('Enter a number'))
for i in range(1,11):
    print(i*no)
'''
'''
5.Write python program to print the pattern given below
Note: Take input from user
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
'''
no=int(input("Enter a number"))
for i in range(1,no+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print('\n')
'''
'''
4.Given the triangle of consecutive odd  numbers
Above triangle is given Calculate Sum row wise 
Example we call function :- row_sum_odd_numbers(2)
Result will be=3 + 5 = 8
if user give 4 then ur output is 13 + 15 + 17+ 19 = 64
'''
'''
no=int(input("Enter a number"))
a=1
b=[]
for i in range(1,no+1):
    for j in range(1,i+1):
        print(a,end=' ')
        if i==no:
            b.append(a)
        a=a+2
    print('\n')
print(sum(b))
'''




















































        

