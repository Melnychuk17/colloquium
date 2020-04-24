# Обчислити суму парних елементів одновимірного масиву до першого
# зустрінутого нульового елемента.
import numpy as np
import random
n=int(input('Enter number of elements: '))
array=np.array([random.randint(-5 ,5) for i in range(n)])
sum=0
for i in range(len(array)):
    if array[i]%2==0:
        sum+=array[i]
        if array[i]==0:
            break
print(array, '\n',sum)
