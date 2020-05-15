#2. Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
#   Expected Outcome:
#   appendMiddle("Chrisdem", IamNewString) → "ChrIamNewStringisdem"


def appendMiddle(x,y):
    I = int(len(s1)/2)
    M = s1[:I-1:] + s2 + s1[-1:]
    print(M)

s1=input("Enter first string: ")
s2=input("Enter Second string: ")
print(appendMiddle(s1,s2))


