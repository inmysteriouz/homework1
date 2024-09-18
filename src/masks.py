def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"**{account_number[-4:]}"


if __name__ == "__main__":

    card_number_str = "1234567890123456"
    account_num = "12345678901234561234"

    print(get_mask_card_number(card_number_str))
    print(get_mask_account(account_num))
