# Лінійний масив містить відомості про кількість опадів, що випали за
# кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість
# опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих
# місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.
import numpy as np
import random
array=np.array([random.randint(0,100) for i in range(12)])
min=100
sum,ser,count,m=0,0,0,0
for i in range(12):
    sum+=array[i]
    if array[i]<30:
        count+=1
    if array[i]<min:
        min=array[i]
        m=i
ser=sum/12
print(array,'\nRainfall: ',sum,'\nAverage rainfall:',ser,'\nThe number of dry months:',count)
if m==0:
    print('January')
elif m==1:
    print('February')
elif m==2:
    print('March')
elif m==3:
    print('April')
elif m==4:
    print('May')
elif m==5:
    print('June')
elif m==6:
    print('July')
elif m==7:
    print('August')
elif m==8:
    print('September')
elif m==9:
    print('October')
elif m==10:
    print('November')
elif m==11:
    print('December')
