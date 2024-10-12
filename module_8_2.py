s = 0
def personal_sum(*numbers):
    global s
    result = 0
    incorrect_data = 0
    if isinstance(numbers[0], list):
        for i in range(len(numbers[0])):
            try:
                result += numbers[0][i]
                s += 1
            except(TypeError):
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {numbers[0][i]}')
                continue
    else:
        raise TypeError
    return (result, incorrect_data)
def calculate_average(*numbers):
    global s
    try:
        result = personal_sum(*numbers)
        sa = result[0] / s
        s = 0
        return sa
    except(ZeroDivisionError):
        s = 0
        return None
    except(TypeError):
        s = 0
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

