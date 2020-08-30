#from watchdog.observer import observer
#from watchdog.events import FileSystemEventHandler
import os 
import json
import time
from pathlib import Path
import re
import shutil

cwd = Path(__file__).parents[0]
os.chdir(cwd)

#a = []
#for files in os.walk('..\\Downloads'):
#    a = list(files)

a = os.listdir('.') # Список файлов в текущей директории
ext = ''
#ext = re.findall(r'.\w+', a[2]) # \w	Любая цифра или буква (\W — все, кроме буквы или цифры)
#print (ext)

for i in range(len(a)):
    ext = re.findall(r'.\w+', a[i])
    ext = ext[-1]
    if ext != '.py':
        os.makedirs(('.\\' + ext), exist_ok=True)
        shutil.move(a[i], ('.\\' + ext))


#def get_files_list():
#    os.walk('')


#class MyHandler(FileSystemEventHandler):
#    i = 1
#    def on_modified(self, event):
#        new_name = 