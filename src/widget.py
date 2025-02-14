from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(tip_number_cart: str) -> str:
    """Функция маски"""

    if not tip_number_cart:
        return "Введите данные..."

    list_number = tip_number_cart.split()

    if list_number[0] == "Счет":
        shifr_card = get_mask_account(list_number[-1])
    else:
        shifr_card = get_mask_card_number(list_number[-1])

    return " ".join(list_number[:-1]) + " " + shifr_card


if __name__ == "__main__":
    print(mask_account_card(""))


def get_date(my_date: str) -> str:
    """Функция перевода формата даты"""

    try:
        date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Введите дату в правильном формате"


if __name__ == "__main__":
    print(get_date(""))
