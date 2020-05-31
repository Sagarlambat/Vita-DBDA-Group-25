#1.Python program to Swap Keys and Values in Dictionary.

o={'a':5, 'b':54, 'c': 5430,'d':45430, 'e':5434, 'f': 230}
d = dict([(value, key) for key, value in o.items()]) 
print ("Original dictionary : ") 
print(d)    
print ("Dictionary after swapping :  ")  
print("keys: values") 
for i in d: 
    print(i, " :  ", d[i]) 


#2.Write program to implement Selection sort.

a=[65,42,31,98,7,548,200,354,629,5654,1,2,0]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            x=a[i]
            a[i]=a[j]
            a[j]=x
    print(a)
print(a)



#3.Write program to implement Insertion sort.

a=[5,3,0,1,7,9,8,2,4,6]
b=[]

for i in range(1, len(a)): 
  
        k = a[i]
        j = i-1
        while j >=0 and k < a[j] : 
                a[j+1] = a[j] 
                j -= 1
        a[j+1] = k 
  
for i in range(len(a)): 
    print ("%d" %a[i],end="")

#4.Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list.
#Given list: list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m",  "n"]
#Sub List to be added = ["h", "i", "j"]
#Expected output:-
#['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']


list1=['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sublist=['h','i','j']
list1[2][1][2].extend(sublist)
print(list1)


#5.Access the value of key “history”
#sampleDict = { 
#   "class":{ 
#      "student":{ 
#         "name":"Mike",
#         "marks":{ 
#            "physics":70,
#            "history":80
#         }
#      }
#   }
#}
#Expected output: 80

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
print(sampleDict['class']['student']['marks']['history'])
