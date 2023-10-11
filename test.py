# def rdng(number):
#     number = str(number)
#     point = number.index('.')
#     temp = number[point + 1:-1]
#
#     if temp[1] in '01234':
#         number = float(number[0:point+3])
#
#         return number
#
#     elif temp[1] in '56789' and '-' in number:
#         number = float(float(number[0:point + 2]) - 0.1)
#
#         return number
#
#     elif temp[1] in '56789' and '-' not in number:
#         number = float(float(number[0:point + 2]) + 0.1)
#
#         return number
#
#
# print(rdng(123.368468994))


# def valid_number(inp_decimal: str):
#     necc_numb = ''
#     if ', ' in inp_decimal:
#         necc_numb = inp_decimal.replace(', ', '.')
#
#     elif ' ,' in inp_decimal:
#         necc_numb = inp_decimal.replace(' ,', '.')
#
#     elif ',' in inp_decimal:
#         necc_numb = inp_decimal.replace(',', '.')
#
#     elif '. ' in inp_decimal:
#         necc_numb = inp_decimal.replace('. ', '.')
#
#     elif ' .' in inp_decimal:
#         necc_numb = inp_decimal.replace(' .', '.')
#
#     elif ' ' in inp_decimal:
#         necc_numb = inp_decimal.replace(' ', '.')
#
#     return necc_numb
#
#
# user = input()
# print(valid_number(user))

# from Utilits import clear, error
# from fractions import Fraction
#
#
# def fract_count_and_out(fractions):
#     output_list = []
#     for op in range(len(fractions) - 1):
#         main_counter = 1
#         fr_counter1 = 1
#         fr_counter2 = 2
#
#         print('+ — сложение;')
#         print('- — вычитание;')
#         print('* — умножение;')
#         print('/ — деление.')
#         while True:
#             print(fractions)
#
#             user_operator = input(f'Введите номер оператора между {fr_counter1} и {fr_counter2} дробями: ')
#
#             if user_operator == '+':
#                 add_fract = fractions[0] + fractions[1]
#                 fractions.pop(0)
#                 fractions.pop(1)
#                 output_list.append(add_fract)
#
#                 main_counter += 1
#                 fr_counter1 += 1
#                 fr_counter2 += 1
#
#             elif user_operator == '-':
#                 add_fract = fractions[0] - fractions[1]
#                 fractions.pop(0)
#                 fractions.pop(1)
#                 output_list.append(add_fract)
#
#                 main_counter += 1
#                 fr_counter1 += 1
#                 fr_counter2 += 1
#
#             elif user_operator == '*':
#                 add_fract = fractions[0] * fractions[1]
#                 fractions.pop(0)
#                 fractions.pop(1)
#                 output_list.append(add_fract)
#
#                 main_counter += 1
#                 fr_counter1 += 1
#                 fr_counter2 += 1
#
#             elif user_operator == '/':
#                 add_fract = fractions[0] / fractions[1]
#                 fractions.pop(0)
#                 fractions.pop(1)
#                 output_list.append(add_fract)
#
#                 main_counter += 1
#                 fr_counter1 += 1
#                 fr_counter2 += 1
#
#             else:
#                 clear()
#                 error()
#
#     clear()
#     print(f'Ответ: {fractions}.')
#
#
# listok = [Fraction(-1, 5), Fraction(5, 34), Fraction(2, 5), Fraction(34, 56)]
# print(fract_count_and_out(listok))


while True:
    fr_counter1 = 1
    fr_counter2 = 2

    print('+ — сложение;')
    print('- — вычитание;')
    print('* — умножение;')
    print('/ — деление.')

    self.user_operator = input(f'Введите номер оператора между {fr_counter1} и {fr_counter2} дробями: ')

    if self.user_operator == '+' or self.user_operator == '-' or self.user_operator == '*' or self.user_operator == '/':
        clear()
        fr_counter1 += 1
        fr_counter2 += 1
        break

    else:
        clear()
        error()












