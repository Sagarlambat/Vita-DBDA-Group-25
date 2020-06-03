import numpy as np
#1.	Write a NumPy program to get the numpy version and
#show numpy build configuration.

print(np.version.version)
print(np.__version__)
print(np.show_config())

#2.Write a NumPy program to test element-wise for complex number, real number of a given array.
#Also test whether a given number is a scalar type or not.

a=np.array([1,2,3,4,5+6j,7+8j])
print(a)
for i in a:
    if np.iscomplex(i):
        print(i,'is a complex number')
    if np.isreal(i):
        print(i,'is real')
    if np.isscalar(i):
        print(i,'is a scalar quantity')

#3.Write a NumPy program to test whether none of the elements
#of a given array is zero.

a=np.array([1,2,3,4,5])
print(all(a))

#4.Write aNumPy program to test whether any of the elements
#of a given array is non-zero.

a=np.array([0,1,2,3,4,0])
print(any(a))

#5.Write a NumPy program to test element-wise for NaN of a given array.

a=np.array([0,1,2,3,4,0,np.nan])
for i in a:
    print(np.isnan(i))

#6.Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal)
#of two given arrays.
a=np.array([1,2,2,4,5])
b=np.array([4,5,2,1,8])
print('checking for greater than')
print(np.greater(a,b))
print('checking for greater than equal to')
print(np.greater_equal(a,b))
print('checking for less than')
print(np.less(a,b))
print('checking for less than equal to')
print(np.less_equal(a,b))

#7.Write a NumPy program to create an element-wise
#comparison (equal, equal within a tolerance) of two given arrays.
#Input:
#x = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
#y = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
x = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])

numpy.allclose() function is used to find if two arrays are element-wise equal within a tolerance. The tolerance values are positive, typically very small numbers. The relative difference (rtol * abs(arr2)) and the absolute difference atol are added together to compare against the absolute difference between arr1 and arr2. If either array contains one or more NaNs, False is returned. Infs are treated as equal if they are in the same place and of the same sign in both arrays.
If the following equation is element-wise True, then allclose returns True.
absolute(arr1 - arr2) <= (atol + rtol * absolute(arr2))
As, The above equation is not symmetric in arr1 and arr2, So, allclose(arr1, arr2) might be different from allclose(arr2, arr1) in some rare cases.
Syntax : numpy.allclose(arr1, arr2, rtol, atol, equal_nan=False)
Parameters :
arr1 : [array_like] Input 1st array.
arr2 : [array_like] Input 2nd array.
rtol : [float] The relative tolerance parameter.
atol : [float] The absolute tolerance parameter.
equal_nan : [bool] Whether to compare NaN’s as equal.
If True, NaN’s in arr1 will be considered
equal to NaN’s in arr2 in the output array.
Return : [ bool] Returns True if the two arrays are equal
within the given tolerance, otherwise it returns False.


rtol=1e-05
atol=1e-08
print(np.allclose(x,y,rtol,atol))

#8.Write a NumPy program to create an array with
#the values 1, 7, 13, 105 and determine the
#size of the memory occupied by the array.

size gives the number of elements
itemsize gives size of each element in memory.

a=np.array([1,7,13,105])
print(a.size*a.itemsize)

#9.Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.

a=np.array([[np.ones(10)],[np.zeros(10)],[np.ones(10)*5]])
print(a)

#10.Write a NumPy program to create an array of the integers from 30 to 70.

a=np.arange(30,71)
print(a)

#11.11.	Write a NumPy program to create an array of all
#the even integers from 30 to 70.

a=np.arange(30,71,2)
print(a)

#12.Write a NumPy program to create a 3x3 identity matrix.

a=np.identity(3)
print(a)

#13.Write a NumPy program to generate a random number between 0 and 1.

a=np.random.normal(0,1)
print(a)

#14.14.	Write a NumPy program to generate an array of 15 random
#numbers from a standard normal distribution.

a=np.random.normal(1,10,15)
print(a)

#15.Write a NumPy program to create a vector with values ranging from 15 to 55 and print all
#values except the first and last.

a=np.arange(15,56)
print(a[1:-1])
