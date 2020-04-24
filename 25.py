# Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
# Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
# 100.
import numpy as np
import random
array=np.array([random.randint(10,100) for i in range(10)])
dob=1
for i in range(len(array)):
    if array[i]%5==0:
        dob*=array[i]
print(array, '\nProduct elements: ', dob)
