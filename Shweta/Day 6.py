'''
#Q1)Python program to swap keys and values in Dictionary
old_dict={"Physics":70,"Maths":80,"Chemistry":90,"Biology":75}
new_dict=dict([(value,key)for key, value in old_dict.items()])
print("old_dict is: ",old_dict)
print("new_dict is: ",new_dict)
'''
'''
#Q2)Write program to implement Selection sort
list=[]
n=int(input("enter a value of n: "))
for x in range(n):
    l=int(input())
    list.append(l)
print("Original list: ",list)
for  i in range(len(list)-1):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print("sorted list", list)
'''     
'''  
#Q3)Write program to implement Insertion sort
list=[]
n=int(input("enter a value of n: "))
for x in range(n):
    l=int(input())
    list.append(l)
print("Original list: ",list)
for i in range(1,len(list)):
    for j in range(i):
        if list[j]>list[i]:
            temp=list[j]
            list[j]=list[i]
            list[i]=temp
            print("sorted list: ",list)
'''
'''
#Q4)Given a nested list extend it with adding sub list["h","i","j"] in a such a way that it will look like
#the following list. Given list=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]..  sub list=["h","i","j"]
#Expected op=['a','b',['c',['d','e',['f','g','h','i','j'],'k',],'l'],'m','n']
list=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
sublist=["h","i","j"]
for i in sublist:
       list[2][1][2].append(i)
print("New list: ",list)
'''
#Q5) Access the value of key "history"
#sampleDict={"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
#expected output: 80
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

