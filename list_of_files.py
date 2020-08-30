import os
from pathlib import Path

cwd = Path(__file__).parents[0]
os.chdir(cwd)

a = []
for files in os.walk('..\\to_4_folders\\0101\\Binary_Low_A'):
    a = list(files)

#c = os.walk('..\\to_4_folders\\0101')
x = a[-1]
#for i in a:
#    a.pop(0)
#a.pop(0)
#.pop(0)

b = 10


print(b)
print(a)
print(b)
print(x)


!!!! просто a = os.listdir('..\\Downloads')

a = os.listdir('.') # Список файлов в текущей директории (где находится скрипт)