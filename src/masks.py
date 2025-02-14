def get_mask_card_number(number_cart: str) -> str:
    """Функция для кодирования номера карты"""

    if number_cart == "":
        return "Введите номер карты"
    number_cart_str = number_cart.split()
    for item in number_cart_str:
        number_cart_digit = ""
        if item.isdigit():
            number_cart_digit += item
            if len(number_cart_digit) == 16:
                return f"{number_cart_digit[:4]} {number_cart_digit[4:6]}** **** {number_cart_digit[12:16]}"
            return "Номер карты должен состоять из 16 цифр"
        return "Номер карты не должен содержать буквы алфавита"
    return "Номер карты должен состоять из 16 цифр"


if __name__ == "__main__":

    print(get_mask_card_number("1234567890933909"))


def get_mask_account(number_score: str) -> str:
    """Функция для кодирования счета карты"""

    number_cart_str = number_score.split()
    for item in number_cart_str:
        number_cart_digit = ""
        if item.isdigit():
            number_cart_digit += item
            if len(number_cart_digit) == 16:
                return f"**{number_score[-4:]}"
            return "Номер карты должен состоять из 16 цифр"
        return "Номер карты не должен содержать буквы алфавита"


if __name__ == "__main__":

    print(get_mask_account("0987653210m00000"))
