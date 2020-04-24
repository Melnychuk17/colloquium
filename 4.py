# Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
# починаються з певної букви, яка вводиться з клавіатури.
array=[input('Enter surname: ') for i in range(5)]
letter=input('1st letter: ')
for i in array:
    for j in i:
        if j[0]==letter:
            print(i)
        else:
            print('Surname is missing')


