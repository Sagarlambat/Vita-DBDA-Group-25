#1.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
'''
l1=[5,2,6,4,3,2,7]
square=[]
result=[]
for i in l1:
    i=i*i
    square.append(i)
print("New list of square no:",square)
'''
#2.From a list containing ints, strings and floats, make three lists to store
#them separately.
'''
l1=[4,2.04,'pratiksha',6,5.25,'hello',4]
integer=[]
s=[]
f=[]
for i in l1:
    if type(i)==int:
        integer.append(i)
    elif type(i)==str:
        s.append(i)
    elif type(i)==float:
        f.append(i)
print("list of integer:",integer)
print("list of String:",s)
print("list of float:",f)
'''
#3.Print the pattern
#1
#1 2 
#1 2 3
#1 2 3 4
#1 2 3 4 5
'''
n=int(input("Enter the no"))
for i in range(1,n+1):
    for j in range(1,i):
        print(j,end="")
    print("\n")
'''

#4.Accept data in two 3*3  matrix and calculate the sum of the matrices.
'''
A=[[4,5,6],[1,2,3],[7,8,9]]
B=[[3,6,9],[2,5,8],[1,4,7]]
add=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        add[i][j]=A[i][j]+B[i][j]
print("The Additon matrix:")
for k in add:
    print(k)
'''
#5.Write a Python program to check whether a given number is a narcissistic number or not
#For example, 371 is a narcissistic number; it has three digits,
#and if we cube each digits  33 + 73 + 13 the sum is 371.

def countDigit(no):
    if (no==0):
        return 0
    else:
        return(1+countDigit(no//10)) 
      
def check(no) : 
    d= countDigit(no) 
    temp = no
    add = 0
    while (temp) : 
        add = add + pow(temp % 10, d) 
        temp = temp // 10
    return (no == add) 
no = int(input("Enter the number"))
if (check(no)) : 
    print( "Number is Narcissistic") 
else : 
    print( "Number is not Narcissistic")




