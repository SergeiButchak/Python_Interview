"""
3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
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


class ItemDiscountReport(ItemDiscount):

    @classmethod
    def get_parent_data(cls):
        return f'Name: {cls.get_name()}, price: {cls.get_price()}'


i = ItemDiscountReport()
print(i.get_parent_data())
