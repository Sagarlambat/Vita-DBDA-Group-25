#1.Write a NumPy program to create a 3X4 array using and iterate over it.
'''
import numpy as np
array=np.arange(0,12).reshape(3,4)
print(array)
print("Elements in array:\n")
for i in np.nditer(array):
  print(i,end=" ")
'''
#2.Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
'''
import numpy as np
array=np.linspace(5,10,50)
print(array)
'''
#3.Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
'''
import numpy as np
array=np.arange(0,21)
print(array)
print("Change the sign of no from 9 to 15")
for i in range(len(array)):
  if array[i]>=9 and array[i]<=15:
    array[i]*=-1
print(array)
'''
#4.Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
'''
import numpy as np
array=np.random.randint(0,11,5)
print("Arbitrary integers from 0 to 10:\n",array)
'''
#5.Write a NumPy program to multiply the values of two given vectors.
'''
import numpy as np
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
c=a*b
print("multiplication of 2 vector")
print(c)
'''
#6.Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
'''
import numpy as np
array=np.arange(10,22).reshape(3,4)
print("Vector of 3*4 from 10 to 21")
print(array)
'''
#7.Write a NumPy program to find the number of rows and columns of a given matrix.
'''
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
s=np.shape(a)
print("Rows and columns of matrix\n",s)
'''
#8.Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.
'''
import numpy as np
array=np.identity(3)

print("Identity matrix of 3*3:\n",array)
'''
#9.Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
'''
import numpy as np
array=np.ones((10,10))
array[1:-1,1:-1]=0

print("Identity matrix of 3*3:\n",array)
'''
#10.Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.
'''
import numpy as np
array=np.ones((5,5))
array=np.diag([1,2,3,4,5])

print("Matrix of 5*5:\n",array)
'''
#11.Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.
'''
import numpy as np
array=np.zeros((4,4))
array[::2,1::2]=1
array[1::2,::2]=1

print("Matrix of 4*4:\n",array)
'''
#12.Write a NumPy program to create a 3x3x3 array filled with arbitrary values.
'''
import numpy as np
array=np.random.random((3,3,3))

print("Matrix of 3*3*3 with arbitrary values:\n",array)
'''
#13.Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array.
'''
import numpy as np
array=np.array([[1,2,3,4],[5,6,7,8]])
print("sum of all elements:\n",np.sum(array))
print("sum of each columns:\n",np.sum(array,axis=0))
print("sum of each rows:\n",np.sum(array,axis=1))
'''
#14.Write a NumPy program to compute the inner product of two given vectors.
#
'''
import numpy as np
array=np.array([2,3])
array1=np.array([3,4])
print(array,"\n",array1)
print("Inner product of vetors:\n",np.dot(array,array1))
'''
#15.Write a NumPy program to add a vector to each row of a given matrix.
'''
import numpy as np
vector=np.array([1,1,1])
array=np.array([[4,5,6],[8,9,7],[10,11,12]])
print("Add a vector is:\n",vector)
print("\nIn which matrix vector to be added each row:\n",array)
result=np.empty_like(array)
for i in range(3):
               result[i,:]=array[i,:]+vector
print("\nAfter adding vector new matrix is:\n",result)
'''               















