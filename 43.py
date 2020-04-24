# Задано два натуральних числа a і b. Змінній w привласнити значення
# істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
# і не кратний b.
import numpy as np
import random
n=int(input('Enter number of elements: '))
array=np.array([random.randint(-10,20) for i in range(n)])
a=int(input('Enter element: '))
b=int(input('Enter element: '))
w=False
for i in range(n):
    if (array[i]%a==0 and array[i]%b!=0):
        w=True
    else:
        w=False
print(array, '\n', w)