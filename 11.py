# Дані про температуру води на Чорноморському узбережжі за декаду
# вересня зберігаються в масиві. Визначити, скільки за цей час було днів, придатних для
# купання.
import numpy as np
import random
array=np.array([random.randint(5,30) for i in range(30)])
count=0
for i in range(30):
    if array[i]>20:
        count+=1
print(array, '\nHot days: ', count)
