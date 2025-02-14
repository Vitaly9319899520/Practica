def filter_by_state(data_logs: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция распределения по спискам"""

    new_list = []

    for i in data_logs:
        if i.get("state") == state:
            new_list.append(i)

    return new_list


if __name__ == "__main__":
    new_list_filter = filter_by_state([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}])
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
                "date": "2018.07.12",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2019.07.12",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018.10.12",
            },
        ],
        reverse=False,
    )
)
