# Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
# екран значення коріння і квадратів кожного з елементів масиву.
x=[int(input('Enter element: ')) for i in range(5)]
k=[i**0.5 for i in x]
v=[i**2 for i in x]
print(x, '\nКорінь: ', k, '\nКвадрат: ', v)