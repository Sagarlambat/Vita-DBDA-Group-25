
#1.
list=[]
n=int(input("Enter the value of n:"))
for x in range(n):
       l=int(input())
       list.append(l)
print("List before sorting:",list)
for i in range(len(list)-1):
       for j in range(len(list)-1-i):
              if list[j]>list[j+1]:
                     temp=list[j]
                     list[j]=list[j+1]
                     list[j+1]=temp
print("Sorted list using bubble sort:",list)

#2.
list=[]
found=False
n=input("Enter the value of n:")
value=input("Enter the value to be searched:")
for i in range(n):
       l=input()
       list.append(l)
print("List",list)
for j in range(len(list)):
             if list[j]==value:
                    found=True
                    print("Value found:",value)
                    break
if found==False:
       print("Value not found")

#3.
list=[]
n=int(input("Enter the value of n:"))
no=int(input("Enter the number to be searched:"))
for i in range(n):
    l=int(input())
    list.append(l)
print("Original list:",list)
print("Sorted list:",list.sort())
lower=0
upper=len(list)
flag=0
while(lower<=upper):
    mid=(lower+upper)//2
    if list[mid]<no:
        lower=mid+1
    elif list[mid]>no:
        upper=mid-1
    else:
        flag=1
        break
if flag==1:
    print("Number found ")
else:
    print("Number not found")
    
#4.
List1 = ["M","na","i","lak"]
List2 = ["y","me","s","han"]
final_list=[]
for i in range (len(List1)):
       final_list.append(List1[i]+List2[i])
print("Final list:",final_list)


#5.                         
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {"John":47,"Peter":64,"Mahi":37,"Maria":76}
for i in roll_number:
    if i not in list(sampledict.values()):
        roll_number.remove(i)
print(roll_number)
