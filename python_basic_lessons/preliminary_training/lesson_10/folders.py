'''
1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
'''

# os.path.join(path, *paths)
# параметры: path - начальный путь, *paths - компоненты пути.
# os.getcwd() - вывод текущей директории

import os

def create_dirs():
    for i in range(1,10):
        #new_folder = os.path.join(os.getcwd(),f"dir_{i}")
        new_folder = f"dir_{i}"
        os.mkdir(new_folder) # для себя чтобы не забыть, это непосрелственно создание папки\директории
def remove_dirs():
    for i in range(1,10):
        #new_folder = os.path.join(os.getcwd(),f"dir_{i}")
        new_folder = f"dir_{i}"
        os.rmdir(new_folder) # для себя чтобы не забыть, это непосрелственно удаление папки\директории

if __name__ == '__main__':
    create_dirs()
    remove_dirs()