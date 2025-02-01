def get_mask_card_number(number_cart: str) -> str:
    """Функция для кодирования номера карты"""

    return f"{number_cart[:5]} {number_cart[5:7]}** **** {number_cart[12:16]}"


if __name__ == "__main__":

    print(get_mask_card_number("1234567890999999"))


def get_mask_account(number_score: str) -> str:
    """Функция для кодирования счета карты"""

    return f"**{number_score[12:16]}"


if __name__ == "__main__":

    print(get_mask_account("0987654321000000"))
