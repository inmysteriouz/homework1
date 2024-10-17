import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    """Фикстура, возвращающая пример списка транзакций для тестирования.
    Включает транзакции с валютами USD и EUR и различными состояниями."""
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2021-01-01T12:00:00",
            "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "Payment 1",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2021-01-02T12:00:00",
            "operationAmount": {"amount": "200.00", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Payment 2",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2021-01-03T12:00:00",
            "operationAmount": {"amount": "300.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "Payment 3",
        },
    ]


def test_filter_by_currency_usd(sample_transactions):
    """
    Тестирует filter_by_currency на фильтрацию транзакций по валюте USD.
    Проверяет, что возвращаются только транзакции с валютой USD.
    """
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 2
    assert usd_transactions[0]["id"] == 1
    assert usd_transactions[1]["id"] == 3


def test_filter_by_currency_no_transactions(sample_transactions):
    """
    Тестирует filter_by_currency на фильтрацию по валюте, которой нет в списке транзакций.
    Проверяет, что для валюты JPY возвращается пустой список.
    """
    jpy_transactions = list(filter_by_currency(sample_transactions, "JPY"))
    assert len(jpy_transactions) == 0


def test_filter_by_currency_empty_list():
    """
    Тестирует filter_by_currency с пустым списком транзакций.
    Убеждается, что возвращается пустой список, если транзакций нет.
    """
    empty_transactions = []
    filtered = list(filter_by_currency(empty_transactions, "USD"))
    assert len(filtered) == 0


def test_transaction_descriptions(sample_transactions):
    """
    Тестирует transaction_descriptions на корректное возвращение описаний транзакций.
    Проверяет, что описания транзакций возвращаются в правильном порядке.
    """
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Payment 1", "Payment 2", "Payment 3"]


def test_transaction_descriptions_empty_list():
    """
    Тестирует transaction_descriptions с пустым списком транзакций.
    Убеждается, что возвращается пустой список, если транзакций нет.
    """
    descriptions = list(transaction_descriptions([]))
    assert descriptions == []


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
    ],
)
def test_card_number_generator(start, end, expected):
    """
    Тестирует card_number_generator на корректное создание номеров карт в диапазоне.
    Использует параметризацию для проверки разных диапазонов номеров.
    """
    assert list(card_number_generator(start, end)) == expected


def test_card_number_generator_single_value():
    """
    Тестирует card_number_generator на генерацию единственного значения.
    Проверяет корректное создание номера карты для одного числа.
    """
    result = list(card_number_generator(1, 1))
    assert result == ["0000 0000 0000 0001"]
