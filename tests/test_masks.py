import pytest
from src.masks import get_mask_card_number, get_mask_account

# Тестирование функции get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234 5678 9012 3456", "1234 56** **** 3456"),  # Стандартный случай с пробелами
        ("1234567890123456", "1234 56** **** 3456"),      # Без пробелов
        ("1234-5678-9012-3456", "1234 56** **** 3456"),   # С дефисами
        ("1234", "****"),                                # Короткий номер
        ("", ""),                                        # Пустая строка
        (None, ""),                                      # None
    ],
)
def test_get_mask_card_number(card_number: str | None, expected: str) -> None:
    """Тестирование функции маскировки номера карты."""
    assert get_mask_card_number(card_number) == expected


# Тестирование функции get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),  # Стандартный случай
        ("1234", "**34"),                    # Короткий номер счета
        ("", ""),                            # Пустая строка
        (None, ""),                          # None
    ],
)
def test_get_mask_account(account_number: str | None, expected: str) -> None:
    """Тестирование функции маскировки номера счета."""
    assert get_mask_account(account_number) == expected
