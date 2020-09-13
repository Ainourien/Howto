
# Перемещает рабочую директорию в местонахождение запускаемого *.py скрипта
    from pathlib import Path
    import os

    cwd = Path(__file__).parents[0]
    os.chdir(cwd)

# Позволяет создать директорию с проверкой существования
    import os
    os.makedirs(('..\\0101'), exist_ok=True)

# Записывает массив в директорию над текущей 
    with open ('..\\0101\\Source.txt', 'w') as f:
        f.write(''.join(ATCG))
        
# Try/Except:
dirs = ['..\\0101\\Binary_Low_A\\', '..\\0101\\Binary_Low_T\\', '..\\0101\\Binary_Low_C\\', '..\\0101\\Binary_Low_G\\']
for i in range(len(dirs)):
    list_of_files = os.listdir(dirs[i])
    try:
        for x in range(len(list_of_files)):
            #Перебираем элементы списка и оставляем только те, названия которых заканчиваются на .txt
            ext = re.findall(r'.\w+', list_of_files[x])          
            ext = ext[-1]        
            if ext != '.txt':
                del list_of_files[x]
        #try/except нужен потому что после удаления элемента списка, количество элементов меняется, а от него зависит количество проходов цикла.
        for j in range(len(list_of_files)):
            zeros_count(dirs[i], str(list_of_files[j])) # Запускаем процедуру, которая создает папку, подсчитывает нули между единицами для каждого файла
    except IndexError:
        pass
