#1.	Write a Python program to sort a list of elements using the bubble sort                                
#Algorithm.

# Python program for implementation of Bubble Sort 

a=[1,2,3,1,55,6,4,5,6,5,4,4,9,9,88,8872,321,5,46]
print("Sample List: ",a)
x=len(a)

for i in range(x-1):
    for j in range(0,x-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("Sorted List: ",a)


#2.Write a Python program for sequential search (Linear search).

a=["python","xyz",2,5,6,4,"lockdown"]
x=input("Enter element to be searched: ")
for i in range(len(a)):
    if a[i]==x:
        print("Element: ",x,"found")
        break
else:
    print("Element not found")



#3.Write a Python program for Binary search.

a=[4,5,6,8,3,2,5,67,8,4,33,1,2,5,7,9]
a=sorted(a)
print(a)
e=int(input('Enter the element to search'))
u=len(a)
l=0
m=(l+u)//2
b=True
while l<u:
     if e==a[m]:
        b=False
        break
     elif e<a[m]:
        u=m-1
        m=(u+l)//2
        print('l=',l,'u=',u,'m=',m)
     elif e>a[m]:
        l=m+1
        m=(u+l)//2
        print('l=',l,'u=',u,'m=',m)
   
print(b)
if b==False:
    print('Element found at index',m)
elif b==True:
    print('Not Found')


#4.Write a python program to concatenate two lists index-wise.
#List1 = [“M”,”na”,”i”,”lak”]
#List2 = [“y”,”me”,”s”,”han”]
#Expected output:
#[“My”,”name”,”is”,”lakhan”]

List1 = ['M','na','i','lak']
List2 = ['y','me','s','han']
x = [i + j for i, j in zip(List1, List2)]
print(x)



#5.Iterate a given list and check if a given element already exists in a
#dictionary as a key’s value if not delete it from the list.
#roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
#sampledict = {“John”:47,”Peter”:64,”Mahi”:37,”Maria”:76}

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {"John":47,"Peter":64,"Mahi":37,"Maria":76}

for i in roll_number:
    if i not in list(sampledict.values()):
        roll_number.remove(i)
        print(i,"is removed")
print(roll_number)
