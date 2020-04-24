# Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
# своїм номером і при цьому кратні 3.
import numpy as np
import random
n=int(input('Enter number of elements: '))
array=np.array([random.randint(-10,20) for i in range(n)])
count=0
for i in range(len(array)):
    if array[i]==i and array[i]%3==0:
        count+=1
print(array,'\n',count)