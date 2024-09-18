from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция маскирует номер карты"""
    if "счет" in number:
        account = number[-20:]
        return number[:20] + get_mask_account(account)
    else:
        number_card = "".join(number[-16:].split())
        return number[-16:] + get_mask_card_number(number_card)


print(mask_account_card("Maestro:1234567890123456"))
print(mask_account_card("Счет:12345678901234567890"))


def get_date(data_info: str) -> str:
    """Функция преобразовывает дату и время"""
    data_time = data_info.split("T")[0]

    return f"{data_time.split('-')[-1]}.{data_time.split('-')[-2]}.{data_time.split('-')[-3]}"


print(get_date("2024-03-11T02:26:18.671407"))
