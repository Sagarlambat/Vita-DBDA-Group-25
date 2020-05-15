sumandaverage="English = 78 science = 83 maths = 68 history = 65"
b=sumandaverage.split()
c=[]
for i in b:
    if i.isnumeric():
        c.append(i)
sum=0
for j in c:
    sum=sum+int(j)
print('sum is:',sum)
percentage=(sum/len(c))
print('percantage is:',percentage)
