#2. Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
#   Expected Outcome:
#   appendMiddle("Chrisdem", IamNewString) → "ChrIamNewStringisdem"


def appendMiddle(x,y):
    return x[:3]+y+x[3:]


s1=input("Enter first string: ")
s2=input("Enter Second string: ")
print(appendMiddle(s1,s2))


