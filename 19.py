# Знайти суму всіх елементів масиву цілих чисел що задовольняють умові:
# остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву
# здійснити випадковими числами від 200 до 300.
import numpy as np
import random
array=np.array([random.randint(200,301) for i in range(20)])
sum=0
for i in range(len(array)):
    if array[i]%2==3:
        sum+=array[i]
print(array, '\nSum elements: ', sum)
