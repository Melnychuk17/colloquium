# Знайти суму всіх елементів масиву цілих чисел, які менше середнього
# арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
# здійснити випадковими числами від 150 до 300.
import numpy as np
import random
array=np.array([random.randint(150,300) for i in range(20)])
sum1=0
ser=0
for i in range(20):
    sum1+=array[i]
ser=sum1/20
sum2=0
for i in range(len(array)):
    if array[i]<ser:
        sum2+=array[i]
print(array, '\nArithmetic mean: ', ser, '\nSum elements: ', sum2)
