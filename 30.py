# Обчислити середнє арифметичне значення тих елементів одновимірного
# масиву, які розташовані за першим по порядку мінімальним елементом.
import numpy as np
import random
n=int(input('Enter number of elements: '))
array=np.array([random.randint(-10 ,20) for i in range(n)])
print(array)
min,min2=0,0
sum,ser=0,0
for i in range(n):
    if array[i]<min:
        min=array[i]
        min2=i
for i in range(n):
    if min2<i:
        ser+=array[i]
ser/=n-min2
print(min, ser, end=', ')

