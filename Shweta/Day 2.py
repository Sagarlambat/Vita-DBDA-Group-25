'''
#Q1)Python program to read a number n and print the series "1+2+.....+n".enter no=4, 1+2+3+4=10
sum=0
n=int(input("enter n:"))
for i in range (1,n+1):
    sum+=i
    if n==i:
        print(i,end='')
    else:
        print(i,end='+')
print("=",sum,sep='')
'''
'''
#Q2)write a program to count the number of even and odd numbers from a series of numbers.
cnt1=cnt2=0
l=[1,2,3,4,5,6,7,8,9]
for i in l:
    if i%2==0:
        cnt1+=1
    else:
        cnt2+=1
print("Even numbers are: ",cnt1,"Odd numbers are: ",cnt2)
'''
'''
#Q3)write a program to creat the multiplication table(from 1 to 10) of a number.
n=int(input("Enter a number: "))
for i in range(1,11):
    p=n*i
    print(n,"*",i,"=",p)
'''
'''
#Q5)write a python program to print the pattern given below. Note:Take input from user
n=int(input("enter a number:"))
for i in range(n+1):
    print((str(i)+' ')*i)
'''
