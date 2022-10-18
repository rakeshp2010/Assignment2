#Using numpy we created an array with 15 random elements

import numpy as np
x = np.random.randint(1,20,15)
print("Generated array:")
print(x)
#Reshape the array to 3 by 5
#Print array shape.


r=np.reshape(x, [3, 5])
print("Shape of the array ",r.shape)
print("Reshaped array: \n",r)

#Replace the max in each row by 0
print("Replaced max in each row by 0")
for i in r:
    i[i == max(i)] = 0
print(r)