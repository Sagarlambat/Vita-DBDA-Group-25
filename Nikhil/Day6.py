#1.Python program to Swap Keys and Values in Dictionary.
'''
a={1:'a',2:'b',3:'c',4:'d'}
b={}
for i in a:
    b[a[i]]=i
print(b)
'''
#2.Write program to implement Selection sort.
'''
a=[22,33,44,55,66,11]
print('a=',a)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
            print(a)
print('sorted list:-',a)
'''
#3.Write program to implement Insertion sort.
'''
a=[12, 11, 13, 5, 6]
for i in range(1,len(a)):
    while a[i-1]>a[i] and i>0:
        print(i)
        a[i],a[i-1]=a[i-1],a[i]
        i-=1
        print(a)
print(a)
'''

#4.Given a nested list extend it with adding sub
'''
list ["h", "i", "j"] in a such a way that it will
look like the following list.
Given list: list1 = ["a", "b", ["c", ["d", "e",["f", "g"], "k"], "l"], "m",  "n"]
Sub List to be added = ["h", "i", "j"]
Expected output:-
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
'''
'''
list1 = ["a", "b", ["c", ["d", "e",["f", "g"], "k"], "l"], "m",  "n"]
s=['h','i','j']
for i in s:
    list1[2][1][2].append(i)
print(list1)
'''
#5.Access the value of key “history”
'''
sampledict = { 
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
print(sampledict['class']['student']['marks']['history'])
'''





















        
