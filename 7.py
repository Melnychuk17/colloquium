# Створіть масив А [1..12] за допомогою генератора випадкових чисел з
# елементами від -20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи
# масиву числом 0.
import random
array=[random.randint(-20,10) for i in range(1,13)]
print('Massif: ', array)
for i in range(len(array)):
    if array[i]<0:
        array[i]=0
print('New massif: ', array)