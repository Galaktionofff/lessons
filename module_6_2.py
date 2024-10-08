class Vehicle:
    def __init__(self, owner:str, model:str, engine_power:int, color:str):
        color_variants = ['blue', 'red', 'green', 'black', 'white']
        Vehicle.__color_variants = color_variants
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{Vehicle.get_model(self)}\n{Vehicle.get_horsepower(self)}'
              f'\n{Vehicle.get_color(self)}\nВладелец:{self.owner}')

    def set_color(self, new_color):
        s = True
        if new_color.lower() in self.__color_variants:
            self.__color = new_color
        else:
            print('Невозможно поставить цвет')


class Sedan(Vehicle):
    _PASSENGER_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
