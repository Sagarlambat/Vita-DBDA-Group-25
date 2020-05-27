#1.Write a Python program to sort a list of elements using the bubble sort                                
#Algorithm.
'''
list1=[2,8,6,9,7,5]
for i  in range(len(list1)-1,0,-1):
    for j in range(i):
        if list1[j]>list1[j+1]:
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
            
print(list1)
'''
#2.Write a Python program for sequential search (Linear search).
'''
import sys
l1=["hello","world",2,8,6,4,"lockdown",2.5,'corona']
z=input("Enter type: ")
x=0
if z=='int':
    x=int(input("Enter element to be searched: "))
elif z=='str':    
    x=input("Enter element to be searched: ")
elif z=='float':
    x=float(input("Enter element to be searched: "))
else:
    print("Please enter correct type (int,str or float)")
    sys.exit()

for i in range(len(l1)):
    if l1[i]==x:
        print("Element: ",x,"found")
        break
else:
    print("Element not found")
'''
#3.Write a Python program for Binary search.
'''
def binary_search(list1,value):
    first=0
    last=len(list1)-1
    search=False
    while(first<=last and not search):
        mid=(first+last)//2
        if list1[mid]==value:
            search=True
        else:
            if value<list1[mid]:
                last=mid-1
            else:
                first=mid+1
    return search
list1=[2,3,5,6,4,8,7,9,1]
value=6
print(binary_search(list1,value))
'''
#4.Write a python program to concatenate two lists index-wise.
'''
list1=['hello ','good ','corona ']
list2=['wrold','morning','virus']
list_concate=[i+j for i,j in zip(list1,list2)]
print("Concatination of two list:",list_concate)
'''
#5.Iterate a given list and check if a given element already exists in a
#dictionary as a key’s value if not delete it from the list.
#roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
#sampledict = {“John”:47,”Peter”:64,”Mahi”:37,”Maria”:76}
'''
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {'John':47,'Peter':64,'Mahi':37,'Maria':76,'cimen':95}

for i in roll_number:
    if i not in list(sampledict.values()):
        roll_number.remove(i)
        print("Removed element is:",i)
    print(roll_number)
    print(sampledict)
'''

