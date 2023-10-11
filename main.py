import time
from Utilits import error, clear
from Fracts import FractOper
from C_and_F import CelsiusAndFahrenheit
from English_system import FromEnglish
from colors import yellow, blue, white


if __name__ == '__main__':
    while True:
        print(f'{blue}1 — операции с дробями;')
        print('2 — операции с °C и °F;')
        print('3 — опеации с английской системой;')
        print(f'4 — выход.{white}')

        main_choice = input('Введите номер действия: ')

        if main_choice == '1' or main_choice == '2' or main_choice == '3' or main_choice == '4':
            clear()
            break

        else:
            clear()
            error()

    if main_choice == '1':
        test = FractOper()
        test.main_fract()

    elif main_choice == '2':
        cel_and_fah_user = CelsiusAndFahrenheit()
        cel_and_fah_user.inp_deg()

    elif main_choice == '3':
        eng_user = FromEnglish()
        eng_user.inp_glmk()

    else:
        print(f'{yellow}Выход...')

        time.sleep(2)

        clear()

