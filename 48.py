# Наведено список прізвищ брокерів товарної біржі з N чоловік. Поміняйте
# місцями прізвища брокерів: першого і останнього, другого і передостаннього, третього
# з початку і третього від кінця і т.д.
import numpy as np
n=int(input('Enter number of boxers: '))
array=np.array([input('Surname: ') for i in range(n)])
print(array, '\n',array[::-1])
