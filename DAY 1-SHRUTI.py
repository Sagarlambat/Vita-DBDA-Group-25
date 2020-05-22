
#1.
list=[]
for i in range(2000,3200):
       if i%7==0 and i%5!=0:
              list.append(i)
print(list)

#2.
d=dict()
n=int(input("Enter the value of n:"))
for i in range(n):
        d[i]=i*i
print(d)

#3.
list=[]
while True:
        l=input("Enter line:")
        if l:
                list.append(l)
        else:
                break
for s in list:
        print(s.upper())


#4.
n=int(input("Enter the value of n:"))
if (n%2==0):
      print("number is even",n)
else:
       print("number is odd:",n)
       
#5.
n=int(input("Enter age:"))
if n>=8 and n<=12:
       print("you are allowed… welcome!!")
else:
       print("Sorry not allowed ..Bye!")

