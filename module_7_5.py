for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(file)
        filetime = os.stat(file).st_ctime #Выводит информацию о последнем изменении файла в секундах
        filetime = time.localtime(filetime) # Подгоняет значение под формат даты и времени
        formatted_time = time.strftime("%d.%m.%Y %H:%M", filetime) # Подгоняет значение под необходимый формат
        filesize = os.path.getsize(file)
        absfile = os.path.abspath(file)# Возвращает абсолютный путь к файлу
        parent_dir = os.path.dirname(absfile)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize}'
                f' байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
