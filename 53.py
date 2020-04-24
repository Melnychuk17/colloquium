# В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
# масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
# п'ятірки. Додаткового масиву не заводити.
import numpy as np
n=int(input('Enter number of elements: '))
array=np.array([int(input('Enter only 0, 1 or 5: ')) for i in range(n)])
print(array,'\n',sorted(array))
