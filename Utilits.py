import os
from colors import red, white


def error():
    print(f'{red}Ошибка ввода: введённые данные некорректны.{white}')


def clear():
    return os.system('cls')


def valid_number(input_decimal):
    necc_numb = ''
    if ', ' in input_decimal:
        necc_numb = input_decimal.replace(', ', '.')

    elif ' ,' in input_decimal:
        necc_numb = input_decimal.replace(' ,', '.')

    elif ',' in input_decimal:
        necc_numb = input_decimal.replace(',', '.')

    elif '. ' in input_decimal:
        necc_numb = input_decimal.replace('. ', '.')

    elif ' .' in input_decimal:
        necc_numb = input_decimal.replace(' .', '.')

    elif ' ' in input_decimal:
        necc_numb = input_decimal.replace(' ', '')

    else:
        return input_decimal

    return necc_numb






