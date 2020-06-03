#1.Write a NumPy program to get the numpy version and show numpy build configuration.
'''
import numpy as np
print(np. __version__)
print(np.show_config())
'''
#2.Write a NumPy program to test element-wise for complex number, real number
#of a given array. Also test whether a given number is a scalar type or not.
'''
import numpy as np
a=np.array([4,5.2,2,3,1j])
print("Original array",a)
print("Complex number:",np.iscomplex(a))
print("Real number:".np.isreal(a))
print("Scalar type:",np.isscalar(a))
'''
#3.Write a NumPy program to test whether none of the elements of a given array
#is zero.
'''
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print("original aaray",a)
print("Check whether any element of array is zero or not")
print(np.all(a))
'''
#4.Write a NumPy program to test whether any of the elements of a given array is non-zero.
'''
import numpy as np
a=np.array([1,2,0,4,0])
print("check any of the element of array is zero or not")
print(np.any(a))
'''
#5.Write a NumPy program to test element-wise for NaN of a given array.

'''
import numpy as np
a=np.array([1,5,6,np.nan])
print("Test element-wise Not a number")
print(np.isnan(a))
'''
#6.Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
'''
import numpy as np
a=np.array([1,5,6])
b=np.array([2,3,4])
print(np.greater(a.b))
print(np.less(a,b))
print(np.greater_equal(a,b))
print(np.less_equal(a,b))
'''
#
#8.Write a NumPy program to create an array with the values 1, 7, 13, 105 and
#determine the size of the memory occupied by the array.
'''
import numpy as np
a=np.array([1,7,13,105])
print("size of the memory occupied is:")
print(a.size*a.itemsize)
'''
#9.Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.
'''
import numpy as np
a=np.zeros(10)
print(a)
a=np.ones(10)
print(a)
a=np.ones(10)*5
print(a)
'''
#10.Write a NumPy program to create an array of the integers from 30 to 70.
'''
import numpy as np
a=np.arange(30,71)
print(a)
'''

#11.Write a NumPy program to create an array of all the even integers from 30 to 70.
'''
import numpy as np
a=np.arange(30,71,2)
print(a)
'''
#12.Write a NumPy program to create a 3x3 identity matrix.
'''
import numpy as np
matrix=np.identity(3)
print("3*3 identity matrix",matrix)
'''

#13.Write a NumPy program to generate a random number between 0 and 1.
'''
import numpy as np
array=np.random.normal(0,1,1)
print("Random number between 0 and 1:\n", array)
'''
#14.Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.
'''
import numpy as np
array=np.random.normal(1,5,15)
print("Random 15 numbers from normal:\n",array)
'''
#15.Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
'''
import numpy as np
array=np.arange(15,55)
print(array)
print("vetctor except the first and last values:\n",array[1:-1])
'''



