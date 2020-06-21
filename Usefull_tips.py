
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