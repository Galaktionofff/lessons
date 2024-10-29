first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


def check(x):
    if len(x[0]) != len(x[1]):
        return x


def check_1(x):
    return len(x[0]) == len(x[1])


def res(x):
    x = len(x[0]) - len(x[1])
    if x < 0:
        x *= -1
    return x


first_result = list(map(res, list(filter(check, list(zip(first, second))))))
print(first_result)
list_ = [(first[x], second[x]) for x in range(len(first))]
second_result = (map(check_1, list_))
print(list(second_result))
