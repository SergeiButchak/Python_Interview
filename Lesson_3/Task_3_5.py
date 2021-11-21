"""
5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод
всех подстрок, состоящих из букв и цифр, например: example345.
"""
import os
import re
import random
import string


def return_word(count):
    while count > 0:
        length = random.randint(1, 10)
        word = ''.join([random.choice(string.ascii_lowercase) for i in range(length)])
        is_need_num = random.randint(0,1)
        if is_need_num == 1:
            word = f'{word}{random.randint(1,1000)}'
        count -= 1
        yield word


def generate_file(name):
    if os.path.isfile(name):
        print('Файл с таким именем уже существует')
        return False
    with open(name, 'w') as file:
        count = random.randint(5, 15)
        number_list = [random.randint(0, 100) for _ in range(count)]
        word_list = [x for x in return_word(count)]
        file.writelines([f'{text} - {number}\n' for number, text in zip(number_list, word_list)])
    read_file(name, 'a', 'o')


def read_file(name, substr=None, replace=None):
    with open(name, 'r') as file:
        lines = [line for line in file]
        for line in lines:
            print(line)
        if substr:
            print(f'Fined substrings "{substr}" in strings:')
            for line in lines:
                sub_str = re.findall(re.compile(substr), line)
                if sub_str:
                    print(line)
                    for s in sub_str:
                        print(s)
                    print('_' * 15)
                    sub_str = []
        if replace:
            print('After replace:')
            for line in lines:
                line = line.replace(substr, replace)
                print(line)


generate_file('5.txt')
