# З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
# що протягом цього часу температура знижувалася. Визначте, о котрій годині було
# вперше зафіксовано від'ємну температуру.
import random
array=[random.randint(-5,20) for i in range(8,21)]
print(array)
b,min=0,0
for i in range(len(array)):
    if array[i]<min:
        min=array[i]
        b=i
        break
print(f'First min t {min} at {b+8} hours')