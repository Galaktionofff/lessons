import os

print('Teкущая директория:', os.getcwd())
if os.path.exists('module_71'):# Позволяет узнать, является ли предложенная директория текущей (Возвращает False или True)
    os.chdir('module_71')# Меняет текущую директорию
else:
    os.mkdir('module_71')# Создает новую директорию
    os.chdir('module_71')
print('Teкущая директория:', os.getcwd())# Позволяет узнать текущую директория
# os.makedirs('2/2')# позволяет создавать вложенные папки
os.chdir('/Users/nikitagalaktionov/PycharmProjects/Urban/NameSpace/.venv/module_7')
os.listdir()# Позволяет посмотреть файлы в текущей директории
for i in os.walk('.'):# Позволяет осмотреть директорию, в том числе вложенные директории
    print(i)
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)
print(file)
os.startfile('/Users/nikitagalaktionov/PycharmProjects/Urban/NameSpace/.venv/module_7/f.txt', operation=open())
