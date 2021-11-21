"""
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в словаре
для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
"""


def get_dict(key_list, value_list):
    res = dict()
    for i in range(len(key_list)):
        try:
            res[key_list[i]] = value_list[i]
        except IndexError:
            res[key_list[i]] = None

    return res


key_list = [f'key_{x}' for x in range(10)]
value_list_eq = [x for x in range(10, 20)]
value_list_lt = [x for x in range(5)]
value_list_gt = [x for x in range(50, 70)]

print(get_dict(key_list, value_list_eq))
print(get_dict(key_list, value_list_lt))
print(get_dict(key_list, value_list_gt))
