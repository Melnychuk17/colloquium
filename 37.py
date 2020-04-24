# Розсортуйте заданий лінійний масив по зростанню.
import numpy as np
import random
array=np.array([random.randint(0,50) for i in range(20)])
print(array)
for i in range(1,len(array)):
    for j in range(len(array)-1,i-1,-1):
        if array[j-1]>array[j]:
            array[j-1],array[j]=array[j],array[j-1]
print(array)