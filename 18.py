# Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
# масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.
import numpy as np
array=np.array([int(input('Enter element: ')) for i in range(10)])
dob=1
for i in range(len(array)):
    if array[i]<0:
        dob*=array[i]
print(array, '\nProduct elements: ', dob)