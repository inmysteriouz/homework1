def get_mask_card_number(card_number: str | None) -> str:
    """Возвращает маскированный номер карты."""
    if not card_number:
        return ""

    cleaned_number = card_number.replace(" ", "").replace("-", "")

    if len(cleaned_number) <= 4:
        return "****"

    return f"{cleaned_number[:4]} {cleaned_number[4:6]}** **** {cleaned_number[-4:]}"


def get_mask_account(account_number: str | None) -> str:
    """Возвращает маскированный номер счета."""
    if not account_number:
        return ""

    if len(account_number) <= 4:
        return "**" + account_number[-2:]

    return "**" + account_number[-4:]


if __name__ == "__main__":
    card_number_str = "1234567890123456"
    account_number_str = "12345678901234561234"

    print(get_mask_card_number(card_number_str))
    print(get_mask_account(account_number_str))
