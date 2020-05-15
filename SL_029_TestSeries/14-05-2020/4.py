#4. Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
#   For Example: –
#   sumAndAverage("English = 78 Science = 83 Math = 68 History = 65") = sum 294 Percentage is 73.5
#   Solution:
#   import r

def sumAndAverage(x):
        a=x.split(" ")
        sum=0
        c=0
        for i in a[2::3]:
            sum+=int(i)
            c+=1
        percentage=(sum/c)    
        return sum,percentage

s,p=sumAndAverage(input("Enter Subject name & marks in following way \nSubject_Name<space>=<space>Marks\nEnglish = 78 Science = 83...so on:\n\n"))

print("sum {} Percentage {}".format(s,p))
            
