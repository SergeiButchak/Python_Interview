"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей
логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:

    __name = 'Laptop'
    __price = 70000


class ItemDiscountReport(ItemDiscount):

    @classmethod
    def get_parent_data(cls):
        return f'Name: {cls.__name}, price: {cls.__price}'


i = ItemDiscountReport()
print(i.get_parent_data())  # AttributeError: 'ItemDiscountReport' object has no attribute '_ItemDiscountReport__name'
