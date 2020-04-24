# Знайти найбільший елемент з елементів одновимірного масиву, що мають
# парний номер. Визначити, чи є він єдиним.
import numpy as np
import random
array=np.array([random.randint(0,20) for i in range(10)])
print(array)
max=0
count=0
for i in range(len(array)):
    if array[i]%2==0:
        if array[i]>max:
            max=array[i]
            count+=1
    if count==1:
        print('Max element sole')
        break
print(max)