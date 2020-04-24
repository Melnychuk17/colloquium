# Змінній t привласнити значення істина, якщо максимальний елемент
# одновимірного масиву єдиний і не перевищує наперед заданого числа а.
import numpy as np
import random
n=int(input('Enter number of elements: '))
array=np.array([random.randint(-10,20) for i in range(n)])
p=int(input('Enter element: '))
count,max=0,0
t=False
for i in range(len(array)):
    if array[i] > max:
        max = array[i]
    if max == array[i]:
        count += 1
if max>p and count>1:
    t = False
else:
    t=True
print(array, '\n',t)