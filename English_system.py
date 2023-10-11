from Utilits import clear, valid_number, error
from colors import green, white, yellow, cyan


class FromEnglish:
    def from_galons(self, galons):
        liters = round(galons * 3.78541, 1)
        print(f'{green}Ответ: {liters} литров(а).{white}')

    def from_liters(self, liters):
        galons = round(liters / 3.78541, 1)
        print(f'{green}Ответ: {galons} галонов(а).{white}')

    def from_miles(self, miles):
        kilometres = round(miles * 1.609344, 1)
        print(f'{green}Ответ: {kilometres} километров(а).{white}')
        
    def from_km(self, kilometres):
        miles = round(kilometres / 1.609344, 1)
        print(f'{green}Ответ: {miles} миль.{white}')
        
    def inp_glmk(self):

        while True:
            while True:
                print(f'{yellow}Для остановки введите *Enter*.{white}')

                print(f'{cyan}1 — из галонов в литры;')
                print('2 — из литров в галоны;')
                print('3 — из миль в километры;')
                print(f'4 — из километров в мили.{white}')

                user_act = input('Выберите действие: ')

                if user_act == '':
                    clear()
                    return False

                if user_act == '1' or user_act == '2' or user_act == '3' or user_act == '4':
                    clear()
                    break

                else:
                    clear()
                    error()

            if user_act == '1':
                while True:
                    user_number = input('Введите число галонов: ')

                    if user_number == '':
                        clear()
                        return False

                    user_number = valid_number(user_number)

                    try:
                        user_number = float(user_number)
                        clear()
                        self.from_galons(user_number)
                        break

                    except:
                        clear()
                        error()

            if user_act == '2':
                while True:
                    user_number = input('Введите число литров: ')

                    if user_number == '':
                        clear()
                        return False

                    user_number = valid_number(user_number)

                    try:
                        user_number = float(user_number)
                        clear()
                        self.from_liters(user_number)
                        break

                    except:
                        clear()
                        error()

            if user_act == '3':
                while True:
                    user_number = input('Введите число миль: ')

                    if user_number == '':
                        clear()
                        return False

                    user_number = valid_number(user_number)

                    try:
                        user_number = float(user_number)
                        clear()
                        self.from_miles(user_number)
                        break

                    except:
                        clear()
                        error()

            if user_act == '4':
                while True:
                    user_number = input('Введите число километров: ')

                    if user_number == '':
                        clear()
                        return False

                    user_number = valid_number(user_number)

                    try:
                        user_number = float(user_number)
                        clear()
                        self.from_km(user_number)
                        break

                    except:
                        clear()
                        error()



