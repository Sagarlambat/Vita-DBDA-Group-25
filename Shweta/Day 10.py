#Q1)write a numpy program to get the numpy version and show numpy build configuration.
import numpy as np
print(np.__version__)
print(np.show_config())

#Q2)Write a NumPy program to test element-wise for complex number, real number of a given array.
#Also test whether a given number is a scalar type or not.
import numpy as np
array=([1,2+1j,3.4,0])
print("complex number is: ",np.iscomplex(array)) #isscalar, iscomplex,isreal is inbuilt function
print("real number is: ",np.isreal(array))
n=3.14
print("scalar number is: ",np.isscalar(n))

#Q3)Write a NumPy program to test whether none of the elements of a given array is zero.
import numpy as np
arr=np.array([1,2,3,4,5])
print(np.all(arr))  #all is used to check non zero element

#Q4)Write a NumPy program to test whether any of the elements of a given array is non-zero.
import numpy as np
arr=np.array([1,0,0,0])
print(np.any(arr))

#Q5)Write a NumPy program to test element-wise for NaN of a given array.
arr=np.array([1,2+2j, 3.4, 3,0,np.nan])
print("Original array:",arr)
print(np.isnan(arr))

#Q6)Write a NumPy program to create an element-wise comparison(greater,greater_equal,less and less_equal)of two given arrays.
import numpy as np
arr1=([1,2,3,4,5])
arr2=([1,6,0,8,10])
print("greater",np.greater(arr1,arr2))
print("greater_equal",np.greater_equal(arr1,arr2))
print("less",np.less(arr1,arr2))
print("less_equal",np.less_equal(arr1,arr2))

#Q7)Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
#Input:x = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
#y = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
import numpy as np
x =np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y =np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print("equal",np.equal(x,y))
print("equal within tolerance",np.allclose(x,y))


#Q8)Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the
#memory occupied by the array.
import numpy as np
arr=np.array([1,7,13,105])
print(arr)
print(arr.size*arr.itemsize) #itemsize give size of each element

#Q9)Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.
import numpy as np
arr1=np.zeros(10)
arr2=np.ones(10)
arr3=np.ones(10)*5
print("array of zeros: ",arr1)
print("array of ones: ",arr2)
print("array of fives: ",arr3)

#Q10)Write a NumPy program to create an array of the integers from 30 to 70.
import numpy as np
array=np.arange(30,71)
print("All integers from 30 to 70 is: ", array)

#Q11)Write a NumPy program to create an array of all the even integers from 30 to 70.
import numpy as np
array=np.arange(30,71,2)
print("All even integers from 30 to 70 is: ", array)

#Q12)Write a NumPy program to create a 3x3 identity matrix.
import numpy as np
array=np.identity(3)
print("3x3 matrix is: ",array)

#Q13)Write a NumPy program to generate a random number between 0 and 1.
import numpy as np
number=np.random.random((0,1,1))
print("random numbers between 0 and 1 is: ",numbers)

#Q14)Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.
import numpy as np
number=np.random.normal((0,1,15))
print("random numbers between 0 and 15 is: ",numbers)

#Q15)Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
import numpy as np
a=np.arange(15,56)
print(a[1:-1])


