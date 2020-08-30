import random
from pathlib import Path
import os

cwd = Path(__file__).parents[0]
os.chdir(cwd)


with open("..\\value\\value_01.txt") as f:
    value = list(f)
    value = value[0].split()

a = len(value)
for i in range(len(value)):
    value.append(float(value[i]))
del value[:a]
    # В 4й строчке вы записываете в переменную "a" целое число:
    # a=random.randint(-5,4)
    # Затем, в 9й строчке вы пытаетесь обратиться к переменной "a" по индексу.
    # a[i]=int(a[i])
    # Но целочисленные переменные не умеют в индекс. Чтобы всё заработало, вам нужно заменить 4ю строчку на такое:
    # a.append(random.randint(-5,4))

print(value)

leather_1 = 285.5
kolichestvo_rulonov_1 = 4
LR_1_list = []
LR_2_list = []
leather_2 = 349.5
kolichestvo_rulonov_2 = 5
summa = 0
# Находим рулоны для первого подрядчика (285.5):
for i in range(500):
    j1 = random.randint(0,len(value)-1)
    j2 = random.randint(0,len(value)-1)
    j3 = random.randint(0,len(value)-1)
    j4 = random.randint(0,len(value)-1)
    if j1!=j2!=j3!=j4:
        summa = value[j1]+value[j2]+value[j3]+value[j4]
        if summa == 285.5:
            print(value[j1], value[j2], value[j3], value[j4])
            LR_1_list = [value[j1], value[j2], value[j3], value[j4]]
      
