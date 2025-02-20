import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("1234567890999999") == "1234 56** **** 9999"


@pytest.mark.parametrize(
    "x,y",
    [
        ("1234567890999", "Номер карты должен состоять из 16 цифр"),
        ("1223424424424242424333", "Номер карты должен состоять из 16 цифр"),
        ("12345678909909k", "Номер карты не должен содержать буквы алфавита"),
    ],
)
def test_get_mask_card_number_len(x, y):
    assert get_mask_card_number(x) == y


def test_get_mask_card_null():
    assert get_mask_card_number("") == "Введите номер карты"


def test_get_mask_card_account():
    assert get_mask_account("0987654321000000") == "**0000"


@pytest.mark.parametrize(
    "x,y",
    [
        ("1234567890999", "Номер карты должен состоять из 16 цифр"),
        ("1223424424424242424333", "Номер карты должен состоять из 16 цифр"),
        ("12345678909909k", "Номер карты не должен содержать буквы алфавита"),
    ],
)
def test_get_mask_card_number_len(x, y):
    assert get_mask_account(x) == y
