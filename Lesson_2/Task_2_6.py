"""
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать
за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.
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


class ItemDiscountReportName(ItemDiscount):

    @classmethod
    def get_info(cls):
        return cls.get_name()


class ItemDiscountReportPrice(ItemDiscount):

    @classmethod
    def get_info(cls):
        return cls.get_price()


print(ItemDiscountReportName.get_info())
print(ItemDiscountReportPrice.get_info())

name = ItemDiscountReportName()
price = ItemDiscountReportPrice()
print(name.get_info())
print(price.get_info())

print(getattr(ItemDiscountReportName, 'get_info')())
print(getattr(ItemDiscountReportPrice, 'get_info')())
