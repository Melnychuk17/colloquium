# Дані про температуру повітря за декаду грудня зберігаються в масиві.
# Визначити, скільки раз температура була вище середньої за цю декаду.
import numpy as np
import random
array=np.array([random.randint(0,20) for i in range(10)])
count,ser,sum=0,0,0
for i in range(10):
    sum+=array[i]
    ser=sum/10
for i in range(len(array)):
    if array[i]>ser:
        count+=1
print(array, '\n',ser, '\n',count)