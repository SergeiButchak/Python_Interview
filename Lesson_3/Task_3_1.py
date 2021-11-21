"""
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением. В функции необходимо реализовать
поиск полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).
"""
import re


def get_file_name(file_path):
    res_dir = re.findall(r'^[\w\\/:]+[\\/](\w+)[.\w]*$', file_path)
    res_file = re.findall(r'(\w+)[.\w]*', file_path)

    if res_dir:
        return res_dir[0]
    elif res_file:
        return res_file[0]
    else:
        return None


print(get_file_name('C:Documents\\text.txt'))
print(get_file_name('/home/sergey/documents/readme.md'))
print(get_file_name('file'))
print(get_file_name('program.exe'))
