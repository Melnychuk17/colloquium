# Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
# одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
# числами від 500 до 1000.
import numpy as np
import random
array=np.array([random.randint(500,1000) for i in range(30)])
sum=0
for i in range(len(array)):
    if array[i]%5==0 or array[i]%8==0:
        sum+=array[i]
print(array, '\nSum elements: ', sum)