# Обчислити середнє арифметичне значення тих елементів одновимірного
# масиву, які потрапляють в інтервал від -2 до 10.
import numpy as np
import random
n=int(input('Enter number of elements: '))
array=np.array([random.randint(-20,20) for i in range(n)])
count,sum,ser=0,0,0
for i in range(len(array)):
    if -2<array[i]<10:
        sum+=array[i]
        count+=1
ser=sum/count
print(array, '\nCount: ',count, '\nMiddle value: ',ser)