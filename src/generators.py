from typing import List, Dict, Iterator, Union, Any
def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Генератор, который фильтрует транзакции по валюте.
    """
    for transaction in transactions:
        if (transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code):
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор, который возвращает описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        card_number = f"{number:016}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number


if __name__ == "__main__":
    transactions: List[Dict[str, Any]] = [
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
            "id": 328390539,
            "state": "CANCELED",
            "date": "2020-08-14T22:18:12.413234",
            "operationAmount": {
                "amount": "12254.93",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод на карту",
            "from": "Счет 53623201863264283103",
            "to": "Счет 58103214602020348139"
        }
    ]

    print("Пример использования filter_by_currency:")
    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(2):
        print(next(usd_transactions))

    print("\nПример использования transaction_descriptions:")
    descriptions = transaction_descriptions(transactions)
    for _ in range(3):
        print(next(descriptions))

    print("\nПример использования card_number_generator:")
    for card_number in card_number_generator(1, 5):
        print(card_number)
