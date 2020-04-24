# Знайти суму додатніх елементів лінійного масиву цілих чисел.
# Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
import numpy as np
array=np.array([int(input('Enter your element: ')) for i in range(10)])
sum=0
for i in range(len(array)):
    if array[i]>0:
        sum += array[i]
print(array,'\nSum + elements: ',sum)