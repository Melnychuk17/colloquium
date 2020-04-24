# Дан одновимірний масив а. Сформувати новий масив, який складається
# тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
# елементів немає, то видати повідомлення.
import numpy as np
import random
n=int(input('Enter number of elements: '))
a=np.array([random.randint(0,15) for i in range(n)])
print(a)
b=[]
for i in range(len(b)):
    if a[i]>i+10:
        b.append(b[i])
if not b:
    print('There are no items')
else:
    print(b)