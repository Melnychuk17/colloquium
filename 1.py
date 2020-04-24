# Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
# один рядок через кому. Отримайте для масиву середнє арифметичне.
# Мельничук Олена 122В
array=[int(input('Enter your element: ')) for i in range(5)]
sum,ser=0,0
for i in range(5):
    sum += array[i]
    ser=sum/5
    print(array[i], end=',')
print('\n',array,'\n',ser)















