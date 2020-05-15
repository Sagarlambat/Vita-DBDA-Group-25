#4. Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
#   For Example: –
#   sumAndAverage("English = 78 Science = 83 Math = 68 History = 65") = sum 294 Percentage is 73.5
#   Solution:

import re
def sumAndAverage(a):
        a=[int(i) for i in re.findall(r'\b\d+\b',a)]
        t=0
        for j in a:
            t+=j

        Percentage = t/len(a)
        return t,Percentage


s,p=sumAndAverage(input("Enter Subject name & marks in following way \nSubject_Name<space>=<space>Marks\nEnglish = 78 Science = 83...so on:\n\n"))

print("sum {} Percentage {}".format(s,p))
            
