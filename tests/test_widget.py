import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def account_card_data() -> list[tuple[str, str]]:
    return [
        ("Maestro: 1234 5678 9012 3456", "Maestro: 1234 56** **** 3456"),
        ("Счет: 12345678901234567890", "Счет: **7890"),
        ("Invalid input", "Invalid input"),
    ]


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Maestro: 1234 5678 9012 3456", "Maestro: 1234 56** **** 3456"),
        ("Invalid input", "Invalid input"),
    ],
)
def test_mask_account_card(number: str, expected: str) -> None:
    assert mask_account_card(number) == expected


@pytest.mark.parametrize(
    "date_info, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("Invalid date", ""),
    ],
)
def test_get_date(date_info: str, expected: str) -> None:
    assert get_date(date_info) == expected
