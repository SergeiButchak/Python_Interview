"""
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:

    __name = 'Laptop'
    __price = 70000

    @classmethod
    def get_name(cls):
        return cls.__name

    @classmethod
    def get_price(cls):
        return cls.__price

    @classmethod
    def set_price(cls, price):
        cls.__price = price


class ItemDiscountReport(ItemDiscount):

    @classmethod
    def get_parent_data(cls):
        return f'Name: {cls.get_name()}, price: {cls.get_price()}'


print(f'{ItemDiscount.__name__} {ItemDiscount.get_price()}')
print(f'{ItemDiscountReport.__name__} {ItemDiscountReport.get_price()}')
print(f'{ItemDiscountReport.get_parent_data()}')
ItemDiscount.set_price(80000)
print(f'{ItemDiscount.__name__} {ItemDiscount.get_price()}')
print(f'{ItemDiscountReport.__name__} {ItemDiscountReport.get_price()}')
print(f'{ItemDiscountReport.get_parent_data()}')
