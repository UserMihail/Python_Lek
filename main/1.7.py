# Примеры использования различных режимов в коде:

# 1. Режим a

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()

# ● data.close() — используется для закрытия файла, чтобы разорвать
# подключение файловой переменной с файлом на диске.

# ● exit() — позволяет не выполнять код, прописанный после этой команды в
# скрипте.

# ● В итоге создаётся текстовый файл с текстом внутри: redbluedreen.

# ● При повторном выполнении скрипта redbluedreenredbluedreen — добавление
# в существующий файл, а не перезапись файлов.

# Ещё один способ записи данных в файл:

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')


# 2. Режим r
# ● Чтение данных из файла:

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

# 3. Режим w


colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()

# ● В итоге создаётся текстовый файл с текстом внутри: ‘redbluedreen’.
# ● В случае перезаписи новые данные записываются, а старые удаляются.


# Модуль os

# Познакомимся с базовыми функциями данного модуля:
# ● os.chdir(path) - смена текущей директории.

import os
os.chdir('C:/Users/79190/PycharmProjects/GB')

# ● os.getcwd() - текущая рабочая директория

import os
print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject

# ● os.path - является вложенным модулем в модуль os и реализует некоторые
# полезные функции для работы с путями, такие как:
# ○ os.path.basename(path) - базовое имя пути

import os
print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) #
'main.py'

# ● os.path.abspath(path) - возвращает нормализованный абсолютный путь.

import os

print(os.path.abspath('main.py'))

# 'C:/Users/79190/PycharmProjects/webproject/main.py'


# Модуль shutil

# Модуль shutil содержит набор функций высокого уровня для обработки файлов,
# групп файлов, и папок. В частности, доступные здесь функции позволяют
# копировать, перемещать и удалять файлы и папки. Часто используется вместе с
# модулем os.
# Для того, чтобы начать работать с данным модулем необходимо его импортировать
# в свою программу:

# import shutil

# Познакомимся с базовыми функциями данного модуля:

# ● shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в
# файл dst.

# ● shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst.
# ● shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path
# должен указывать на директорию, а не на символическую ссылку.
