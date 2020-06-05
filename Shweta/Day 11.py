				    
#Q1)Write a NumPy program to create a 3X4 array using and iterate over it.
import numpy as np
v=np.arange(0,12).reshape(3,4)
print("original array:", v)
for i in np.nditer(v):
    print(i)

#Q2)Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
import numpy as np
vector=np.linspace(5,50,10)
print(vector)

#Q3)Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the
#range from 9 to 15.
import numpy as np
v=np.arange(0,21)
print(v)
for i in range (len(v)):
    if v[i]>=9 and v[i]<=15:
        v[i]=v[i]*-1
print(v)

#Q4)Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
import numpy as np
v=np.random.randint(0, 11, 5) #take random variable in  given range
print(v)

#Q5)Write a NumPy program to multiply the values of two given vectors.
import numpy as np
v1=np.arange(0,5)
print("first vector is: ",v1)
v2=np.arange(10,15)
print("second vector is: ",v2)
print("Multiplied vectord is: ",v1*v2)

#Q6)Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
import numpy as np
v=np.arange(10,22).reshape(3,4)
print("3x4 matrix is:",v)

#Q7)Write a NumPy program to find the number of rows and columns of a given matrix.
import numpy as np
v=np.arange(0,12).reshape(3,4)
print("Row and Column size is:",v.shape)

#Q8)Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.
import numpy as np
array=np.identity(3)
print("3x3 matrix is: ",array)

#Q9)Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1,and inside 0.
import numpy as np
v=np.ones(10,10)
v[1:-1,1:-1]=0
print(v)

#Q10)Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.
import numpy as np
v=np.diag([1,2,3,4,5])
print(v)

#Q11)Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal
import numpy as np
v=np.diag([0,0,0,0])
v[::2, 1::2] = 1
v[1::2, ::2] = 1
print(v)

#Q12)Write a NumPy program to create a 3x3x3 array filled with arbitrary values.
import numpy as np
v=np.random.random((3,3,3))#used to take random arbitary values
print(v)

#Q13)Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array. 
import numpy as np
arr=np.arange(0,12).reshape(2,6)
print(arr)
print("Sum of each column:",arr.sum(axis=0))
print("Sum of each row:",arr.sum(axis=1))

#Q14)Write a NumPy program to compute the inner product of two given vectors.
import numpy as np
arr1=np.arange(0,5)
arr2=np.arange(6,11)
print(arr1)
print(arr2)
new_arr=np.dot(arr1,arr2)
print("Dot product of two vectors is:",new_arr)

#Q15)Write a NumPy program to add a vector to each row of a given matrix
import numpy as np
m = np.array([[0,1,2], [3,4,5], [6,7,8]])
v = np.array([1, 2, 3])
print("Original vector:",v)
print("Original matrix:",m)
final_result = np.empty_like(m) 
for i in range(3):
       final_result[i, :] = m[i, :] + v
print("After adding the vector a new matrix is:",final_result)

