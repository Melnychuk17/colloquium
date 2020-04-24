# Дані про температуру повітря за декаду листопада зберігаються в масиві.
# Визначити, скільки разів температура опускалася нижче -10 градусів.
import numpy as np
import random
array=np.array([random.randint(-15,10) for i in range(31)])
count=0
for i in range(31):
    if array[i]<-10:
        count+=1
print(array, '\nThe number of elements < -10: ', count)
