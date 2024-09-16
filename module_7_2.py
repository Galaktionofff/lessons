from pprint import pprint
def  custom_write(file_name, strings):
    strings_position = {}
    for i in range(len(strings)):
        s = open(file_name, 'a')
        s.write(f'{strings[i]}\n')
        strings_position[i, s.tell()] = strings[i]
    return strings_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
