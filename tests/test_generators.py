import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2021-01-01T12:00:00",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Payment 1"
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2021-01-02T12:00:00",
            "operationAmount": {
                "amount": "200.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Payment 2"
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2021-01-03T12:00:00",
            "operationAmount": {
                "amount": "300.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Payment 3"
        }
    ]

def test_filter_by_currency_usd(sample_transactions):
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 2
    assert usd_transactions[0]["id"] == 1
    assert usd_transactions[1]["id"] == 3

def test_filter_by_currency_no_transactions(sample_transactions):
    jpy_transactions = list(filter_by_currency(sample_transactions, "JPY"))
    assert len(jpy_transactions) == 0

def test_filter_by_currency_empty_list():
    empty_transactions = []
    filtered = list(filter_by_currency(empty_transactions, "USD"))
    assert len(filtered) == 0

def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Payment 1", "Payment 2", "Payment 3"]

def test_transaction_descriptions_empty_list():
    descriptions = list(transaction_descriptions([]))
    assert descriptions == []

@pytest.mark.parametrize("start,end,expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"])
])
def test_card_number_generator(start, end, expected):
    assert list(card_number_generator(start, end)) == expected

def test_card_number_generator_single_value():
    result = list(card_number_generator(1, 1))
    assert result == ["0000 0000 0000 0001"]
