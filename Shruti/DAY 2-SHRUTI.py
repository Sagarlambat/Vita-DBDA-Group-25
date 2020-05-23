#1.
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
       sum=sum+i
       if n==i:
              print(i,end='')
       else:
              print(i,end='+')
print('=',sum, sep='')

#2.
n=int(input("Enter a number:"))
numbers=[]
even_nos=0
odd_nos=0
for i in range(n):
       l=int(input())
       if (l%2==0):
              even_nos+=1
       else:
              odd_nos+=1
       numbers.append(l)
print("Numbers:",numbers)
print("Number of even numbers : ",even_nos)
print("Number of odd numbers : ",odd_nos)

#3.
n=int(input("Enter a number:"))
print("Multiplication table of ",n,"is")
for i in range(1,11):
       product=n*i
       print(n,"*",i,"=",product)

#5.
n=int(input("Enter a number"))
for i in range(n+1):
       print((str(i)+'')*i)



