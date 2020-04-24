# У лінійному масиві знайти максимальний елемент. Вставте порядковий
# номер елемента за ним, пересунувши всі залишилися на одну позицію вправо.
import numpy as np
import random
array=np.array([random.randint(-10,10) for i in range(20)])
print(array)
b=0
max=0
number=[]
for i in range(len(array)):
    number.append(array[i])
for i in range(len(array)):
    if array[i]>max:
        max=array[i]
        b=i
number.insert(b+1,b)
print('Max element: ',max,'\nOn position',b,'\nMassif',number)

