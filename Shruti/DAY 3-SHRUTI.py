
#1.
list=[]
new_list=[]
n=int(input("Enter the value of n:"))
for i in range(n):
            l=int(input())
            list.append(l)
print("List:",list)
for j in (list):
       s=j*j
       new_list.append(s)
print("new_list:",new_list)


#2.
list=[1,'abc',2.5,'xyz',4,6.6]
int_list=[]
string_list=[]
float_list=[]
for i in (list):
       if type(i)==int:
              int_list.append(i)
       elif type(i)==float:
              float_list.append(i)
       elif type(i)==str:
              string_list.append(i)
print("List containing int:",int_list)
print("List containing string:",string_list)
print("List containing float:",float_list)


#3.
n=int(input("Enter the value of n:"))
for i in range(n):
       for j in range(i+1):
              print(str(j+1),end=' ')
       print()

#5.
sum=0
n=int(input("enter a number"))
s=n
if (n>=100 and n<=999):
       while(n!=0):
              r=n%10
              sum=sum+(r*r*r)
              n=n//10
elif (n>=1000 and n<=9999):
       while(n!=0):
              r=n%10
              sum=sum+(r*r*r*r)
              n=n//10
if sum==s:
       print("narcissistic no")
else:
       print("Not")
           
