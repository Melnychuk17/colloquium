# Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
# Заповнення масиву здійснити випадковими числами від 5 до 500.
import numpy as np
import random
array=np.array([random.randint(5,500) for i in range(10)])
dob=1
for i in range(len(array)):
    if array[i]%3==0 or array[i]%9==0:
        dob*=array[i]
print(array, '\nProduct elements: ', dob)