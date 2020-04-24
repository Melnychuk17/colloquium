# Знайти кількість парних елементів одновимірного масиву до першого
# зустрінутого числа рівного наперед заданому числу а.
import numpy as np
import random
n=int(input('Enter number of elements: '))
array=np.array([random.randint(0,20) for i in range(n)])
print(array)
a=int(input('Enter element: '))
count=0
for i in range(len(array)):
        if array[i]%2==0:
            count+=1
            if array[i]==a:
                count-=1 # відняли 1 елемент щоб не включати в к-сть вказаний елемент
                break
print('Number of paired elements: ', count)

