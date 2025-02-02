from datetime import datetime

import masks


def mask_account_card(tip_number_cart: str) -> str:
    """Функция маски"""

    list_number = tip_number_cart.split()
    #print(list_number)

    if list_number[0] == 'Счет':
        shifr_card = masks.get_mask_account(list_number[-1])
    else:
        shifr_card = masks.get_mask_card_number(list_number[-1])


    return  ' '.join(list_number[:-1]) + " " + shifr_card


print(mask_account_card("Мир 1234567890123456"))


def get_date(my_date: str) -> str:
    """Функция перевода формата даты"""

    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
