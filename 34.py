# Дано два лінійних масиву однакової розмірності. Скласти третій масив з
# добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.
import numpy as np
import random
n=int(input('Enter number of elements: '))
array=np.array([random.randint(-10,20) for i in range(n)])
array2=np.array([random.randint(-10,20) for j in range(n)])
arr=np.zeros(n,dtype=int)
for i in range(n):
   arr[i]=array[i]*array2[i]
print(array,'\n',array2,'\n',arr)






