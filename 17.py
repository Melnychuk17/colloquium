# Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
# Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100
# до 200.
import numpy as np
import random
array=np.array([random.randint(100,201) for i in range(20)])
sum=0
for i in range(len(array)):
    if array[i]%2==1:
        sum+=array[i]
print(array, '\nSum pair elements: ', sum)