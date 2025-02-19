from typing import Iterator, List, Dict

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[Dict]:
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item


usd_transactions = filter_by_currency(transactions, "USD")
print(next(usd_transactions))
print(next(usd_transactions))
print(next(usd_transactions))


def transaction_descriptions(transactions:list[dict]) -> Iterator[str]:
    for i in transactions:
        for k,v in i.items():
            if k == 'description':
                yield v


desc_transactions = transaction_descriptions(transactions)
print(next(desc_transactions))
print(next(desc_transactions))
print(next(desc_transactions))


def card_number_generator(start,stop):
    for number in range(start,stop+1):
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
