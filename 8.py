# Створіть цілочисельний масив А [1..15] за допомогою генератора
# випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
# найбільший елемент масиву і його індекс.
import random
array=[random.randint(-15,30) for i in range(1,16)]
max=0
index=0
for i in range(len(array)):
    if array[i]>max:
        max=array[i]
        index=i
print(array, '\nLargest element: ', max, index)
