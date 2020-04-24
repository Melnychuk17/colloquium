# Створіть масив з 15 цілочисельних елементів і визначте серед них
# мінімальне значення.
array=[int(input('Enter your element: ')) for i in range(15)]
min=0
for i in range(len(array)):
    if array[i]<min:
        min=array[i]
print(array, '\nLeast element: ', min)
