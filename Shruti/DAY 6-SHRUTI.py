
#1.
d=dict()
n=int(input("Enter the value of n:"))
for i in range(n):
       d[i]=input()
print("Dictionary",d)
d = {value:key for key, value in d.items()}
print("Swapped dictionary:",d)

#2.
list=[]
n=int(input("Enter the value of n:"))
for i in range(n):
       l=int(input())
       list.append(l)
print("Original list:",list)
for i in range(len(list)-1):
       for j in range(i+1,len(list)-1):
              if list[i]>list[j]:
                     t=list[i]
                     list[i]=list[j]
                     list[j]=t
print("Sorted list:",list)

#3.
list=[]
n=int(input("Enter the value of n:"))
for i in range(n):
       l=int(input())
       list.append(l)
print("Original list:",list)
for i in range(1,len(list)):
       for j in range(i):
              if list[j]>list[i]:
                     t=list[j]
                     list[j]=list[i]
                     list[i]=t
print("Sorted list:",list)                     


#4.
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m",  "n"]
Sub_List = ["h", "i", "j"]
for i in Sub_List:
       list1[2][1][2].append(i)
print("New_list:",list1)


#5.
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print( sampleDict['class']['student']['marks']['history'])

