
#1.
import numpy as np
x = np.arange(10,22).reshape((3, 4))
print("Original array:")
print(x)
print("Each element of the array is:")
for i in np.nditer(x):
  print(i,end=" ")


#2.
import numpy as np
x=np.linspace(5,50,10)
print(x)

#3.
import numpy as np
x=np.arange(0,21)
print("Values from 0 to 20:",x)
for i in range(len(x)):
       if (x[i]>=9 and x[i]<=15):
              x[i]*=-1
print("After changing sign:",x)

#4.
import numpy as np
x=np.linspace(0,10,5)
print(x)

#5.
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=x*y
print("Product:",z)

#6.
import numpy as np
x=np.arange(10,22)
print(x)
print("3*4 matrix:",x.reshape(3,4))

#7.
import numpy as np
x=np.arange(10,35).reshape(5,5)
print(x)
print("Number of rows and columns:",x.shape)

#8.
import numpy as np
x=np.identity(3)
print("3*3 identity matrix\n:",x)

#9.
import numpy as np
x=np.ones((10,10))
x[1:-1, 1:-1]=0
print("Final matrix:\n",x)

#10.
import numpy as np
x=np.diag([1,2,3,4,5])
print(x)

#11.
import numpy as np
x = np.zeros((4, 4))
x[0::2, 1::2] = 1
x[1::2, 0::2] = 1
print(x)

#12.
import numpy as np
x=np.random.random((3,3,3))
print(x)

#13.
import numpy as np
x=np.arange(1,11).reshape(2,5)
print(x)
print("Sum of each column:",x.sum(axis=0))
print("Sum of each row:",x.sum(axis=1))

#14.
import numpy as np
x=np.arange(1,6)
y=np.arange(6,11)
print(x)
print(y)
z=np.dot(x,y)
print("Dot product:",z)

#15.
import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
b = np.array([1, 1, 0])
print("Original vector:")
print(b)
print("Original matrix:")
print(a)
result = np.empty_like(a) 
for i in range(4):
       result[i, :] = a[i, :] + b
print("\nAfter adding the vector b to each row of the matrix a:")
print(result)
