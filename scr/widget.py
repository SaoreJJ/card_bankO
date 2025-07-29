from masks import get_mask_card_number, get_mask_account

def mask_account_card(input_str: str) -> str:
    """
    Маскирует номер карты/счета в строке формата "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"
    Возвращает строку с сохранением названия и маскированным номером
    """
    if 'счет' in input_str.lower():
        # Обработка счета
        parts = input_str.split()
        return f"{' '.join(parts[:-1])} {get_mask_account(parts[-1])}"
    else:
        # Обработка карты
        parts = input_str.split()
        return f"{' '.join(parts[:-1])} {get_mask_card_number(parts[-1])}"


