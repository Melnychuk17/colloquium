# Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
# однаковими значеннями.
import numpy as np
array=np.array([int(input('Enter element: ')) for i in range(20)])
print(array)
for i in range(20):
    if len(array)>len(set(array)):
        print('There are same elements')
        break
    else:
        print('Elements are different')
        break
