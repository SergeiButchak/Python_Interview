"""
5. Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная
ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию подсчета процентов
для пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев. Вложенная функция возвращает сумму
дополнительно внесенных средств (с процентами), а главная функция — общую сумму по вкладу на конец периода.
"""


def process_account(fee, period, replenishment):

    def additional_perc(replenishment, period, perc):
        return replenishment * sum([(1 + perc / 12 / 100)**x for x in range(1, period - 1)]) * (1 + perc / 12 / 100)

    products = [
        {
            'begin_sum': 1000,
            'end_sum': 10000,
            6: 5,
            12: 6,
            24: 5
        },
        {
            'begin_sum': 10000,
            'end_sum': 100000,
            6: 6,
            12: 7,
            24: 6.5
        },
        {
            'begin_sum': 100000,
            'end_sum': 1000000,
            6: 7,
            12: 8,
            24: 7.5
        },
    ]

    prod = None
    for p in products:
        if p['begin_sum'] <= fee < p['end_sum']:
            prod = p

    if prod is None:
        return 0
    try:
        return fee * ((1 + prod[period] / 12 / 100) ** period) + additional_perc(replenishment, period, prod[period])  # Вариант с ежемесячной капитализацией
    except KeyError:
        return -1


print(process_account(10000, 12, 0))  # Онлайн калькулятор 10 722.90 руб.
print(process_account(10000, 12, 5000))   # Онлайн калькулятор 62658.54 руб.
