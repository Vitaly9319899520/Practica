def get_mask_card_number(number_cart: str) -> str:
    """Функция для кодирования номера карты"""

    return f"{number_cart[:4]} {number_cart[4:6]}** **** {number_cart[12:16]}"


if __name__ == "__main__":

    print(get_mask_card_number("1234567890999999"))


def get_mask_account(number_score: str) -> str:
    """Функция для кодирования счета карты"""

    return f"**{number_score[-4:]}"


if __name__ == "__main__":

    print(get_mask_account("0987654321001111"))
