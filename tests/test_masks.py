import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234 5678 9012 3456", "1234 56** **** 3456"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234-5678-9012-3456", "1234 56** **** 3456"),
        ("1234", "****"),
        ("", ""),
        (None, ""),
    ],
)
def test_get_mask_card_number(card_number: str | None, expected: str) -> None:
    """Тестирование функции маскировки номера карты."""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        ("1234", "**34"),
        ("", ""),
        (None, ""),
    ],
)
def test_get_mask_account(account_number: str | None, expected: str) -> None:
    """Тестирование функции маскировки номера счета."""
    assert get_mask_account(account_number) == expected
