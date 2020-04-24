# Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
# числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
# від 50 до 100.
import numpy as np
array=[np.random.randint(50,100) for i in range(10)]
a=int(input('Enter number: '))
dob=1
for i in range(len(array)):
    if array[i]<a:
        dob*=array[i]
print(array, '\nSum elements: ', dob)