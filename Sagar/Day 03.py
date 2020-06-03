#1.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.

a=[1,2,3,4,5,6,7,8,9]
b=[i**2 for i in a]
print(b)


#2.From a list containing ints, strings and floats, make three lists to store them separately. 


a=["a",1,2.56,"b","c",5,6,7.77]
ints=[]
strings=[]
floats=[]
for i in a:
    if type(i)==int:
        ints.append(i)
    elif type(i)==str:
        strings.append(i)
    else:
        floats.append(i)
print(ints)
print(strings)
print(floats)


#3.Print the pattern
#1
#1 2 
#1 2 3
#1 2 3 4
#1 2 3 4 5


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print("")


#4.Accept data in two 3*3  matrix and calculate the sum of the matrices.

'''
x=[[1,1,1],[1,1,1],[1,1,1]]
y=[[1,2,3],[4,5,6],[7,8,9]]
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

    
#5.Write a Python program to check whether a given number is a narcissistic number or not
#For example, 371 is a narcissistic number; it has three digits, and if we cube each digits  33 + 73 + 13 the sum is 371.
#Other 3-digit narcissistic numbers are
#153 = 13 + 53 + 33
#370 = 33 + 73 + 03
#407 = 43 + 03 + 73.
#There are also 4-digit narcissistic numbers, some of which are 1634, 8208, 9474 since
#1634 = 14+64+34+44
#8208 = 84+24+04+84
#9474 = 94+44+74+44


a=int(input("Enter a number: "))
n=len(str(a))
s=""
b=0
for i in str(a):
    b+=int(i)**n
print(str(b))
if b == a:
    print("The given number is a narcissistic number")
else:
    print("The given number is not a narcissistic number")


