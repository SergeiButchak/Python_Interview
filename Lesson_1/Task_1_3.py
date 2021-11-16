"""
3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться
по шаблону: “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""
import time


def random(start, end):
    rng = end - start
    tm = round(time.time())
    seed = tm
    a = 45
    m = seed % 10000
    c = 11
    while True:
        seed = (a * seed + c) % m
        res = seed % rng + start
        yield res if res != 0 else res + 1


r = random(-50, 50)
lst = []
dct = {}
for i in range(30):
    lst.append(next(r))
    dct[f'elem_{i}'] = next(r)

print(lst)
print(dct)
