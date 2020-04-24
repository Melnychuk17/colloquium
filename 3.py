#Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
#починаючи з останнього.
array=[input('Enter surname: ') for i in range(5)]
for i in array[::-1]:
    print(i)