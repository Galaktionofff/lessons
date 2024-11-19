import time
import threading
from queue import Queue
from random import randint

q = Queue()
tables_guests = {}


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

    def __str__(self):
        return f'Стол номер {self.number}'


class Guest(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def run(self):
        time.sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        queue = Queue()
        self.queue = queue

    def guest_arrival(self, *guests):
        for i in range(len(guests)):
            guests = list(guests)
            self.g = guests.pop(0)
            for table in self.tables:
                if table.guest == None:
                    table.guest = self.g
                    print(f"{table.guest} сел(-а) за стол номер {table.number}")
                    self.g.start()
                    break
                elif table.guest != None and i < 5:
                    continue
                else:
                    self.queue.put(self.g)
                    print(f"{self.g} в очереди")
                    break

    def discuss_guests(self):
        global tables
        global tables_guests
        while not self.queue.empty or [True for tab in tables if not tab.guest == None]:
            for table in tables:
                if table.guest != None and not table.guest.is_alive():
                    print(f'{table.guest} покушал(-а) и ушёл(ушла)" и "Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and [True for tab in tables if tab.guest == None]:
                    table.guest = self.queue.get()
                    print(f"{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    table.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
