# Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
# масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
import numpy as np
import random
array=np.array([random.randint(10,51) for i in range(15)])
dob=1
for i in range(len(array)):
    if array[i]%7==0:
        dob*=array[i]
print(array, '\nProduct elements: ', dob)