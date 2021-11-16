"""
Дополнить следующую функцию недостающим кодом:
"""
import os


def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """

    if os.path.exists(sPath):
        if os.path.isdir(sPath):
            file_list = os.listdir(sPath)
            for file in file_list:
                if os.path.isfile(os.path.join(sPath, file)):
                    print(os.path.join(sPath, file))
                elif os.path.isdir(os.path.join(sPath, file)):
                    print_directory_contents(os.path.join(sPath, file))
        else:
            return
    else:
        print(f'Каталог "{sPath}" не найден.')


print_directory_contents(os.path.dirname(os.path.abspath(__file__)))
print_directory_contents('/home/sergey/projects/PycharmProjects/Python_Interview')
print_directory_contents('Моя папка')
