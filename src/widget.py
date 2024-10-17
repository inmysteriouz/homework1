from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция маскирует номер счета или карты"""
    if "счет" in number.lower():
        account = number[-20:]
        return f"{number[:20]}{get_mask_account(account)}"
    elif "maestro" in number.lower() or "visa" in number.lower() or "mastercard" in number.lower():
        clean_number = number.split(": ")[1].replace(" ", "")
        masked_card = get_mask_card_number(clean_number)
        return f"{number.split(': ')[0]}: {masked_card}"
    else:
        return number


def get_date(date_info: str) -> str:
    """Функция преобразует дату из формата 'YYYY-MM-DDTHH:MM:SS' в 'DD.MM.YYYY'"""
    try:
        date_part = date_info.split("T")[0]
        year, month, day = date_part.split("-")
        return f"{day}.{month}.{year}"
    except ValueError:
        return ""


if __name__ == "__main__":
    print(mask_account_card("Maestro: 1234 5678 9012 3456"))
    print(mask_account_card("Счет: 12345678901234567890"))
    print(get_date("2024-03-11T02:26:18.671407"))
