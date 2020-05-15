#3. Arrange String characters such that lowercase letters should come first
#Given input String of combination of the lower and upper case arrange characters in such a way that all lowercase letters should come first.
#Expected Output:
#input_String = PyNaTive
#arranging characters giving precedence to lowercase letters
#aeiNPTvy
#arranging characters giving precedence to lowercase letters:
#yaivePNT


input_string=input("Enter a String having combination of uppercase & lowercase characters: ")
x,y="",""
for i in input_string:
    if i.islower():
        x+=i
    elif i.isupper():
        y+=i
print("arranging characters giving precedence to lowercase letters:\n",x+y)
