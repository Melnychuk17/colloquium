# Підрахувати кількість елементів одновимірного масиву, для яких
# виконується нерівність i*i<ai<i!
import numpy as np
import math
n=int(input('Enter number of elements: '))
array=np.array([int(input('Enter element: ')) for i in range(n)])
count=0
for i in range(n):
    if i*i<i<math.factorial(i):
        count+=1
print(array,'\n',count)