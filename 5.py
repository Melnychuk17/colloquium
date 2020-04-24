# Створіть масив А [1..7] за допомогою генератора випадкових чисел і
# виведіть його на екран. Збільште всі його елементи в 2 рази.
import random
array=[random.randint(0,20) for i in range(1,8)]
k=[i*2 for i in array]
print(array, '\nNew massif: ',k)

