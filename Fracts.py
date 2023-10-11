from Utilits import error, clear
from colors import white, yellow
from fractions import Fraction


class FractOper:
    def __init__(self):
        self.fractions = []
        self.user_operator = ''
        self.counter = 1
        self.first_fract = 0
        self.second_fract = 0

    def main_fract(self):
        while True:
            print(f'{yellow}Для остановки введите *Enter*.{white}')

            user_num = input(f'Введите числитель {self.counter} дроби: ')

            if user_num == '':
                clear()
                return False

            try:
                user_num = int(user_num)
                clear()
                break

            except:
                clear()
                error()

        while True:
            user_denum = input(f'Введите знаменатель {self.counter} дроби: ')

            if user_denum == '':
                clear()
                return False

            try:
                user_denum = int(user_denum)
                self.first_fract = Fraction(user_num, user_denum)
                self.counter += 1
                clear()
                break

            except:
                clear()
                error()

        self.add_fract()

    def add_fract(self):
        while True:
            print(self.first_fract)

            while True:
                print('+ — сложение;')
                print('- — вычитание;')
                print('* — умножение;')
                print('/ — деление.')

                print(f'{yellow}Для остановки введите *Enter*.{white}')

                self.user_operator = input('Введите символ оператора: ')

                if self.user_operator == '':
                    clear()
                    return False

                if self.user_operator == '+' or self.user_operator == '-' or self.user_operator == '*' or self.user_operator == '/':
                    clear()
                    break

                else:
                    clear()
                    error()

            while True:
                print(f'{yellow}Для остановки введите *Enter*.{white}')

                add_num = input(f'Введите числитель {self.counter} дроби: ')

                if add_num == '':
                    clear()
                    return False

                try:
                    add_num = int(add_num)
                    clear()
                    break

                except:
                    clear()
                    error()

            while True:
                add_denum = input(f'Введите знаменатель {self.counter} дроби: ')

                if add_denum == '':
                    clear()
                    return False

                try:
                    add_denum = int(add_denum)
                    self.second_fract = Fraction(add_num, add_denum)
                    self.counter += 1
                    clear()
                    break


                except:
                    clear()
                    error()

            if self.user_operator == '+':
                self.first_fract = self.first_fract + self.second_fract

            elif self.user_operator == '-':
                self.first_fract = self.first_fract - self.second_fract

            elif self.user_operator == '*':
                self.first_fract = self.first_fract * self.second_fract

            elif self.user_operator == '/':
                self.first_fract = self.first_fract / self.second_fract