import time
import threading
from queue import Queue
from random import randint
q = Queue()

class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest
        self.__str__()

    def __str__(self):
        print(f'Стол номер {self.number}')
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
        queue = Queue
        self.queue = queue

    def guest_arrival(self, *guests):
        global tables
        g = 0
        for table in tables:
            if table.guest == None:
                guests = list(guests)
                g = guests.pop(0)
                g.Guest.start()
            else:
                self.queue.put(g, g)

    def discuss_guest(self):
        if 






tables = [Table(number) for number in range(1, 6)]
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
print(tables)
