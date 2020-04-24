# Змінній t привласнити значення істина, якщо в одновимірному масиві є
# хоча б одне від’ємне і парне число.
import numpy as np
import random
n=int(input('Enter number of elements: '))
array=np.array([random.randint(-10,20) for i in range(n)])
t=False
for i in range(len(array)):
    if array[i]<0 or array[i]%2==0:
        t=True
print(array, '\n',t)