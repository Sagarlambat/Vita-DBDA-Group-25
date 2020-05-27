'''
#Q1) write a program to sort a list of elements using the bubble sortnalgorithm. 
list=[]
n=int(input("Enter the numbers: "))
for x in range(n):
    l=int(input())
    list.append(l)
print("Original list: ",list)
def sort(list):
    for i in range(len(list)-1,0,-1):   # here we take list-1 bcz list start from 0,if we give 5 it will iterate0 to 4
        for j in range(i):              # it will iterate values of i
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
sort (list)
print(list)'''

'''
#Q2) Write a program for sequential search(linear search)
list=[]
n=int(input("Enter the numbers: "))
for x in range(n):
    l=int(input())
    list.append(l)
s=int(input("enter element for search:"))
print("list: ",list)
for i in range(len(list)):
    if list[i]==s:
        print("Number found")
if s not in list:
    print("Not found")
'''
'''
#Q3) write a program for binary search.
list=[25,66,80,1,6]
list.sort()
print("sorted list: ",list)
no=int(input("enter a number: "))

def Binary_search(list,no):
    low=0
    high=len(list)-1
    Found=False
    while low<=high and not Found:
        mid=(low+high)//2
        if no==list[mid]:
            Found=True
        elif no>=list[mid]:
            low=mid+1
        else:
            high=mid-1
    if Found==True:
        print("Number is found")
    else:
        print("Number is not found")
Binary_search(list,no)
'''
'''
#Q4) write a proram to concatenate two listsindex-wise.
list1=['M','na','i','lak']
list2=['y','me','s','han']
new_list=[]
for i in range(len(list1)):
    new_list.append(list1[i]+list2[i])
print(new_list)
'''

#Q5)Iterate a given list and check if a given element already exists in a dictionary as a keys value
#if not delete it from the list.
roll_number=[47,64,69,37,76,83,95,97]
sampledict={"John":47,"Peter":64,"Mahi":37,"Maria":76,"cimen":95}
for i in roll_number:
    if i not in list(sampledict.values()):
        roll_number.remove(i)
print(roll_number)

