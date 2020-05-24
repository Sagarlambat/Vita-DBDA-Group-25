#1.You are given with a list of integer elements.
#Make a new list which will store square of elements of previous list.
'''
a=[1,2,3,4,5]
b=[i**2 for i in a]
print(b)
'''
#2.From a list containing ints, strings and floats,
#make three lists to store them separately. 
'''
a=[1,2,'a','nikhil',1.22,3.4444]
int1=[]
float1=[]
str1=[]
for i in a:
    if str(i).isdigit():
        int1.append(i)
    elif str(i).isalpha():
        str1.append(i)
    elif isinstance(i,float):#type(i)==floAT
        float1.append(i)
print(str1,'\n',int1,'\n',float1)        
'''
#3.Print the pattern
'''
1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5

n=int(input('Enter a number'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print('\n')
'''

#4.Accept data in two 3*3  matrix and calculate the sum of the matrices.
'''
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
X=[]
Y=[]
v=[]

print("\nEnter elements for Matrix 1:")
for p in range(R):           
    x =[] 
    for q in range(C):       
         x.append(int(input())) 
    X.append(x)
print("Matrix 1 = ",X)

print("\nEnter elements for Matrix 2:")
for s in range(R):          
    y =[] 
    for t in range(C):       
         y.append(int(input())) 
    Y.append(y)
print("Matrix 2 = ",Y)

for i in range(len(x)):
    n=[]
    for j in range(len(X[i])):
        n.append(X[i][j]+Y[i][j])
    v.append(n)
print("\nResult = ",v)




'''
#5Write a Python program to check whether a given number is a narcissistic number or not
#For example, 371 is a narcissistic number; it has three digits, and if we cube each digits  33 + 73 + 13 the sum is 371. Other 3-digit narcissistic numbers are
#153 = 13 + 53 + 33
#370 = 33 + 73 + 03
#407 = 43 + 03 + 73.
#There are also 4-digit narcissistic numbers, some of which are 1634, 8208, 9474 since
#1634 = 14+64+34+44
#8208 = 84+24+04+84
#9474 = 94+44+74+44
'''
a=int(input('enter a number'))
n=a
sum=0
while(n!=0):
    b=n%10
    sum=sum+b**(len(str(a)))
    n=n//10
print(sum)
if sum==a:
    print('narcissistic')
else:
    print('not narcissistic')
'''











