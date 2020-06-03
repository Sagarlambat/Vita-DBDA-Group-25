
#1.
import numpy as np
print(np.__version__)
print(np.show_config())


#2.
import numpy as np
x=np.array([2+2j, 1.5, 3, 8, 1+1j])
print("Original array:",x)
print("Complex numbers:\n")
for i in(x):
       if  np.iscomplex(i):
              print()
print("Real numbers:\n")
for i in(x):
       if np.isreal(i):
              print(i)

#3.
import numpy as np
x=np.array([2+2j, 1.5, 3, 8, 1+1j])
print("Original array:",x)
print(np.alls(x))

#4.
import numpy as np
x=np.array([2+2j, 1.5, 3, 8, 1+1j])
print("Original array:",x)
print(np.any(x))

#5.
import numpy as np
x=np.array([2+2j, 1.5, 3, 8, 1+1j,np.nan])
print("Original array:",x)
print(np.isnan(x))

#6.
import numpy as np
x=np.array([4,5,2,7,3])
y=np.array([7,6,9,8,1])
print("Greater comparison:",(np.greater(x,y)))
print("Greater equal comparison:",(np.greater_equal(x,y)))
print("Less comparison:",(np.less(x,y)))
print("Less equal comparison:",(np.less_equal(x,y)))

#7.
import numpy as np
x=np.array([4,5,2,7,3])
y=np.array([7,6,9,8,1])
print("Equal comparison:",(np.equal(x,y)))
print("Equal within a tolerance comparison:",(np.allclose(x,y)))

#8.
import numpy as np
x=np.array([1, 7, 13, 105])
print("Size of memory occupied by array",(x.itemsize*x.size))

#9.
import numpy as np
x=np.zeros(10)
print("Array of 10 zeros:",x)
x=np.ones(10)
print("Array of 10 ones:",x)
x=np.ones(10)*5
print("Array of 10 fives:",x)

#10.
import numpy as np
x=np.arange(30,71)
print("Array of integers from 30 to 71:",x)

#11.
import numpy as np
x=np.arange(30,71,2)
print("Array of even integers:",x)

#12.
import numpy as np
x=np.identity(3)
print("3*3 identity matrix\n",x)


#13.
import numpy as np
x=np.random.normal(0,1,1)
print("random number between 0 and 1:",x)

#14.

import numpy as np
x=np.random.normal(0,1,15)
print("Random numbers from a standard normal distribution:",x)

#15.
import numpy as np
x=np.arange(15,55)
print(x)
print("Numbers between 15 to 55 except the first and the last one:",x[1:-1])
