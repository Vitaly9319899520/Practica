def filter_by_state(data_logs: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция распределения по спискам"""

    new_list = []

    for i in data_logs:
        if i.get("state") == state:
            new_list.append(i)

    return new_list


if __name__ == "__main__":
    new_list_filter = filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
    print(new_list_filter)


def sort_by_data(data_logs: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортировки по дате"""

    return sorted(data_logs, key=lambda x: x["date"], reverse=reverse)


print(
    sort_by_data(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
)


def card_number_generator(start, stop):
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