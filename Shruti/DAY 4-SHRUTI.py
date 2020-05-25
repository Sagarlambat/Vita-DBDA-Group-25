
#1.
def max(x,y,z):
       if x>y:
              if x>z:
                     return x
              else:
                     return z
       else:
              return y

#3.
def sum(no):
      if no==1:
             return 1
      else:
      return (no+sum(no-1))


#4.
def showStudent(student_name,student_id="1",college_name="VITA"):
       print("Hello",student_name,"your id is",student_id,"your collge name is",college_name)             

#5.
def unique(*data):
       return (set(data))

#6.
no=int(input("Enter a number:"))
def first_digit(no):
       first=no
       while first>=10:
              first=first//10
       return first
def last_digit(no):
       last=no%10
       return last
print("Sum of first and last digits of no is:",first_digit(no)+last_digit(no))
       

       

