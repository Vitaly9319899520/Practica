from typing import Iterator, List, Dict
from data import transactions


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[Dict]:

"""Функция нахождения транзакции по коду валюты"""

    
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item


usd_transactions = filter_by_currency(transactions, "USD")
print(next(usd_transactions, 'Нет данных'))
print(next(usd_transactions, 'Нет данных'))
print(next(usd_transactions, 'Нет данных'))


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:

"""Функция нахождения значения транзакции"""|

    
    for i in transactions:
        for k, v in i.items():
            if k == "description":
                yield v


desc_transactions = transaction_descriptions(transactions)
print(next(desc_transactions))
print(next(desc_transactions))
print(next(desc_transactions))


def card_number_generator(start, stop):

"""Функция генератор номера карты"""

    
    for number in range(start, stop + 1):
        str_number = str(number)
        if len(str_number) < 16:
            number1 = "0" * (16 - len(str_number)) + str_number
        else:
            number1 = str_number

        number_card = f"{number1[:4]} {number1[4:8]} {number1[8:12]} {number1[12:16]}"

        yield number_card


gen = card_number_generator(9999997, 9999999)
print(next(gen))
print(next(gen))
print(next(gen))
