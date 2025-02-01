from datetime import datetime

import masks


def mask_account_card(tip_number_cart: str) -> str:
    """Функция маски"""

    digit_card = ""
    alpha_card = ""
    list_number = tip_number_cart.split()

    if (
        " ".join(list_number[:2]) == "Visa Platinum"
        or "Maestro" in list_number
        or " ".join(list_number[:2]) == "Visa Classic"
        or " ".join(list_number[:2]) == "Visa Gold"
        or "MasterCard" in list_number
    ):

        for i in list_number:
            if i.isalpha():
                alpha_card += i + " "
                # alpha_card.append(i)

            elif i.isdigit():
                digit_card += i
            shifr_card = masks.get_mask_card_number(digit_card)

    elif "Счет" in list_number:
        for i in list_number:
            if i.isalpha():
                alpha_card += i
            elif i.isdigit():
                digit_card += i
            shifr_card = masks.get_mask_account(digit_card)

    return f"{alpha_card} {shifr_card}"


print(mask_account_card("MasterCard 7000792289606361"))


def get_date(my_date: str) -> str:
    """Функция перевода формата даты"""

    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
