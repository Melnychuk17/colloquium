# Напишіть програму аналізу значень температури хворого за добу:
# визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
# температури виробляються шість раз на добу і результати вводяться з клавіатури у
# масив T.
import numpy as np
T=np.array([float(input('Enter t: ')) for i in range(6)])
min,max,sum,ser=40,35,0,0
for i in range(6):
    if T[i]>max:
        max=T[i]
    if T[i]<min:
        min=T[i]
    sum+=T[i]
ser=sum/6
print(T,'\nMiddle t: ',ser,'\nMin t: ',min,'\nMax t: ',max)




