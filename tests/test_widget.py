import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card():
    assert mask_account_card("Мир 1234567890123456") == "Мир 1234 56** **** 3456"


@pytest.mark.parametrize(
    "x,y",
    [
        ("Мир 1234567890123456", "Мир 1234 56** **** 3456"),
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("Счет 1234567890123456", "Счет **3456"),
    ],
)
def test_get_mask_card_number_len(x, y):
    assert mask_account_card(x) == y


def test_get_mask_card_number_len():
    assert mask_account_card("") == "Введите данные..."


def test_get_data():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),  # корректная дата
        ("2024-03-11", "Введите дату в правильном формате"),  # некорректный формат
        ("", "Введите дату в правильном формате"),  # пустая строка
        ("2024-03-11T02:26:18", "Введите дату в правильном формате"),  # без миллисекунд
    ],
)
def test_get_date(input_date, expected_output):
    assert get_date(input_date) == expected_output


def test_get_date_null():
    assert get_date("") == "Введите дату в правильном формате"
