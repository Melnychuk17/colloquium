# У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
# виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
import random
n=int(input('Enter number of ticket: '))
array=[random.randint(1,100) for i in range(10)]
print(array)
for i in range(10):
    if n in array:
        print('Win')
        break
    else:
        print('Losing')
        break

