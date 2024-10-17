import pytest
from src.generators import filter_by_currency


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 987654321,
            "state": "PENDING",
            "date": "2020-01-01T12:00:00",
            "operationAmount": {
                "amount": "500.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Оплата услуг",
            "from": "Счет 123456789",
            "to": "Счет 987654321"
        }
    ]


def test_filter_by_currency_usd(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    result = list(usd_transactions)

    assert len(result) == 2
    assert all(tx["operationAmount"]["currency"]["code"] == "USD" for tx in result)


def test_filter_by_currency_no_matching(transactions):
    gbp_transactions = filter_by_currency(transactions, "GBP")
    result = list(gbp_transactions)

    assert len(result) == 0


def test_filter_by_currency_empty_list():
    empty_transactions = []
    usd_transactions = filter_by_currency(empty_transactions, "USD")

    result = list(usd_transactions)
    assert len(result) == 0


def test_filter_by_currency_no_currency_match(transactions):
    jpy_transactions = filter_by_currency(transactions, "JPY")

    result = list(jpy_transactions)
    assert len(result) == 0


@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 2),
    ("EUR", 1),
    ("JPY", 0)
])
def test_filter_by_currency_parametrized(transactions, currency, expected_count):
    filtered_transactions = filter_by_currency(transactions, currency)
    result = list(filtered_transactions)

    assert len(result) == expected_count
