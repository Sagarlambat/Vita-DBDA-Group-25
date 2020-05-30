#1.Python program to Swap Keys and Values in Dictionary.
'''
ldict={'abc':11,'pqr':12,'xyz':13,'mno':14,'stu':15}
new_dict={}
new_dict = dict([(value,key) for key, value in ldict.items()])
print(new_dict)
'''
#2.Write program to implement Selection sort.


#3.Write program to implement Insertion sort.
'''
list1=[]
no=int(input("Enter the no of list element"))
for i in range(no):
    l1=int(input("Enter element"))
    list1.append(l1)
print(list1)
for i in range(1,len(list1)):
    for j in range(i):
        if list1[j]>list1[i]:
            temp=list1[j]
            list1[j]=list1[i]
            list1[i]=temp
print("Sorted list is:",list1)
'''    
#4.Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list.
#Given list: list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m",  "n"]
#Sub List to be added = ["h", "i", "j"]
#Expected output:-['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
'''
list1=['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sublist=['h','i','j']
list1[2][1][2].extend(sublist)
print(list1)
'''
#5.Access the value of key “history”
'''sampleDict = { 
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
Expected output: 80
'''
'''
sample_dict={"class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print("Access the specific value of key:",sample_dict['class']['student']['marks']['history'])
'''
