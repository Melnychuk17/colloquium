# Знайти суму всіх елементів масиву дійсних чисел, більших за задане
# число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
# від 50 до 100.
import numpy as np
import random
array=np.array([random.randint(50,101) for i in range(20)])
a=int(input('Enter number: '))
sum=0
for i in range(len(array)):
    if array[i]>a:
        sum+=array[i]
print(array, '\nSum elements: ', sum)

