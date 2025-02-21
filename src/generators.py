from typing import Dict, Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[Dict]:
    """Функция нахождения транзакции по коду валюты"""

    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item
        else:
            raise ValueError("Нет транзакций")


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Функция нахождения значения транзакции"""

    if len(transactions) == 0:
        raise ValueError("Нет транзакций")

    for i in transactions:
        for k, v in i.items():
            if k == "description":
                yield v


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Функция генератор номера карты"""

    if start > stop:

        raise ValueError("Ошибка: Start не должен превышать Stop")

    else:

        for number in range(start, stop + 1):
            str_number = str(number)
            if len(str_number) < 16:
                number1 = "0" * (16 - len(str_number)) + str_number
            else:
                number1 = str_number

            number_card = f"{number1[:4]} {number1[4:8]} {number1[8:12]} {number1[12:16]}"

            yield number_card
