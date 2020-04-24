# Створіть масив А [1..8] за допомогою генератора випадкових чисел з
# елементами від -10 до 10 і виведіть його на екран. Підрахуйте кількість від’ємних
# елементів масиву.
import random
array=[random.randint(-10,10) for i in range(1,9)]
count=0
for i in array:
    if i<0:
        count+=1
print('Massif: ', array, '\nThe number of negative elements: ', count)
