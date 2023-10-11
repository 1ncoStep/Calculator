from Utilits import error, clear, valid_number
from colors import green, white, yellow


class CelsiusAndFahrenheit:
    def from_c_logic(self, c):
        f = round(c * 1.8 + 32, 1)

        print(f'{green}Ответ: {f}°F.{white}')

    def from_f_logic(self, f):
        c = round((f - 32) / 1.8, 1)

        print(f'{green}Ответ: {c}°C.{white}')

    def inp_deg(self):
        while True:

            print('1 — Из Цельсия в Фаренгейт;')
            print('2 — из Фаренгейта в Цельсия.')

            while True:
                print(f'{yellow}Для остановки введите *Enter*.{white}')
                user_number = input('Выберите действие: ')

                if user_number == '':
                    clear()
                    return False

                if user_number == '1' or user_number == '2':
                    clear()
                    break

                else:
                    clear()
                    error()

            if user_number == '1':

                while True:
                    user_c = input('Введите градусы Цельсия: ')

                    if user_c == '':
                        clear()
                        return False

                    user_c = valid_number(user_c)

                    try:
                        user_c = float(user_c)
                        clear()
                        self.from_c_logic(user_c)
                        break

                    except:
                        clear()
                        error()

            elif user_number == '2':

                while True:
                    user_f = input('Введите градусы Фаренгейта: ')

                    if user_f == '':
                        clear()
                        return False

                    user_f = valid_number(user_f)

                    try:
                        clear()
                        user_f = float(user_f)
                        self.from_f_logic(user_f)
                        break

                    except:
                        clear()
                        error()









