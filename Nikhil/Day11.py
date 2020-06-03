import numpy as np
#1.Write a NumPy program to create a 3X4 array using and iterate over it.
'''
a=np.linspace(1,12,12).reshape(3,4)
print(a)
for i in np.nditer(a):
    print(i)
'''
#2.Write a NumPy program to create a vector of length 10 with values
#evenly distributed between 5 and 50.
'''
a=np.linspace(5,50,10)
print(a)
'''
#3.Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in
#the range from 9 to 15.
a=np.arange(0,21)
'''
for i in range(len(a)):
    if  a[i] >=9 and a[i]<=15:
      a[i]=a[i]*-1
print(a)
'''
#4.Write a NumPy program to create a vector of length 5 filled
#with arbitrary integers from 0 to 10.
'''
a=np.random.randint(0,11,5)
print(a)
'''
#5.Write a NumPy program to multiply the values of two given vectors.
'''
a=np.arange(1,5)
print(a)
b=np.arange(6,10)
print(b)
print(a*b)
'''
#6.Write a NumPy program to create a 3x4 matrix filled with
#values from 10 to 21.
'''
a=np.arange(10,22).reshape(3,4)
print(a)
'''
#7.Write a NumPy program to find the number of rows and columns of a given matrix.
'''
a=np.arange(10,22).reshape(3,4)
print(a.shape)
'''
#8.Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1,
#the rest are 0.
'''
a=np.identity(3)
print(a)
'''
#9.Write a NumPy program to create a 10x10 matrix, in which the elements
#on the borders will be equal to 1 ,and inside 0.
'''
a=np.ones((10,10))
a[1:-1,1:-1]=0
print(a)
'''
#or
'''
a=np.zeros((10,10))
a[:,0],a[0,:],a[-1,:],a[:,-1]=1,1,1,1
print(a)
'''
#10.Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.
'''
a=np.diag([1,2,3,4,5])
print(a)
'''
#11.Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered,
#with zeros on the main diagonal.
'''
a=np.diag([0,0,0,0])
a[0::2,1::2]=1
a[1::2,0::2]=1
print(a)
'''
#12.Write a NumPy program to create a 3x3x3 array filled with arbitrary values.
'''
a=np.random.random((3,3,3))
print(a)
'''
#13.Write a NumPy program to compute sum of all elements,
#sum of each column and sum of each row of a given array. 
'''
a=np.linspace(10,90,9).reshape(3,3)
print(a)
print('sum=',np.sum(a))
print('sum of each columns',np.sum(a,axis=0))
print('sum of each row=',np.sum(a,axis=1))
'''
#14.Write a NumPy program to compute the inner product of two given vectors.
'''
a=np.array([1,2,3,4])
b=np.array([1,2,3,4])
print(np.dot(a,b))
'''
#15.Write a NumPy program to add a vector to each row of a given matrix.
a=np.array([[1,2,3,4],[5,6,7,8]])
v=[1,1,1,1]
res=np.empty_like(a)
i,j=np.shape(a)
print(i)
for k in range(i):
    res[k,:]=a[k,:]+v
print(res)




























