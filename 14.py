# Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
# пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с.
import numpy as np
array=np.zeros(10)
for i in range(10):
    h=(9.8 * i**2) / 2
    array[i]=h
    print(f'Distance after {i+1} seconds : {h} meters')

