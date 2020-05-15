#1. Given a number count the total number of digits in a number
#   For example: The number is 75869, so the output should be
#   Reverse the following list using for loop
#   list1 = [10, 20, 30, 40, 50]
#   Expected output:
#   50
#   40
#   30
#   20
#   10

#1.a

a=int(input("Enter a number: "))
print(len(str(a)))

print("\n")

#1.b
list1 = input("Enter a list numbers or elements separated by space: ").split()
for i in list1[::-1]:
        print(i)







