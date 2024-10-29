from random import choice
first = 'Мама мыла раму'
second = 'Рамена мало было'
res = list(map(lambda x, y: x == y, first, second))
print(res)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as w:
            for words in data_set:
                if isinstance(words, str):
                    w.write(f'{words} ')
                else:
                    for word in words:
                        w.write(f'{str(word)} ')

    return write_everything

write = get_advanced_writer('example.txt')

write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *word):
        self.word = word

    def __call__(self):
        return choice(self.word)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
