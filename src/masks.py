def get_mask_card_number(card_number: str | None) -> str:
    if not card_number:
        return ""

    # Убираем пробелы и дефисы, чтобы унифицировать формат
    cleaned_number = card_number.replace(" ", "").replace("-", "")

    # Если длина меньше 4, возвращаем "****"
    if len(cleaned_number) <= 4:
        return "****"

    # Маскируем цифры, кроме первых 4 и последних 4
    return f"{cleaned_number[:4]} {cleaned_number[4:6]}** **** {cleaned_number[-4:]}"


def get_mask_account(account_number: str | None) -> str:
    if not account_number:
        return ""

    # Если длина номера счета меньше 4 символов
    if len(account_number) <= 4:
        return "**" + account_number[-2:]

    # Маскируем все, кроме последних 4 символов
    return "**" + account_number[-4:]


if __name__ == "__main__":
    # Примеры номеров карты и счета
    card_number_str = "1234567890123456"
    account_number_str = "12345678901234561234"

    # Вывод маскированных номеров
    print(get_mask_card_number(card_number_str))
    print(get_mask_account(account_number_str))
