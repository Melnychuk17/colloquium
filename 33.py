# Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
import numpy as np
import random
array=np.array([random.randint(-10 ,10) for i in range(20)])
dob=1
for i in range(len(array)):
    if array[i]!=0:
        dob*=array[i]
print(array, '\n',dob)




