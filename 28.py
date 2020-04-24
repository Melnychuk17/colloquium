# Знайти кількість парних елементів одновимірного масиву.
import numpy as np
import random
n=int(input('Enter number of elements: '))
array=np.array([random.randint(-100,100) for i in range(n)])
count=0
for i in range(len(array)):
    if array[i]%2==0:
        count+=1
print(array, '\nNumber of paired elements: ', count)