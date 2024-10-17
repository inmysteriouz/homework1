from typing import List, Dict, Iterator

Transaction = Dict[str, any]


def filter_by_currency(transactions: List[Transaction], currency_code: str) -> Iterator[Transaction]:
    """
    Функция фильтрует транзакции по коду валюты и возвращает итератор.
    """
    return (transaction for transaction in transactions
            if transaction["operationAmount"]["currency"]["code"] == currency_code)


if __name__ == "__main__":
    transactions = [
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

    usd_transactions = filter_by_currency(transactions, "USD")

    for _ in range(2):
        print(next(usd_transactions))
