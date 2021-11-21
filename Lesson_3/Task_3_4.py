"""
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл. Если файл
с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить два списка:
с текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом, чтобы каждая строка
файла содержала текстовое и числовое значение. Вызвать вторую функцию. В нее должна передаваться ссылка на созданный
файл. Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого. Вся программа
должна запускаться по вызову первой функции.
"""
import os
import random
import string


def return_word(count):
    while count > 0:
        length = random.randint(1, 10)
        word = ''.join([random.choice(string.ascii_lowercase) for i in range(length)])
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
    read_file(name)


def read_file(name):
    with open(name, 'r') as file:
        for line in file:
            print(line)


generate_file('4.txt')
