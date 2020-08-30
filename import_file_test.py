import os
from pathlib import Path
cwd = Path(__file__).parents[0]
os.chdir(cwd)

a = []

with open (('1.txt'), 'r') as f:
    a = list(f)

a = a[0].split()
print(a)
