import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power, count_of_enemy = 100):
        super().__init__()
        self.name = name
        self.power = power
        self.count_of_enemy = count_of_enemy
        self.__str__()

    def __str__(self):
        print(f'{self.name} на нас напали!')

    def run(self):
        days = 0
        while self.count_of_enemy:
            time.sleep(1)
            days += 1
            self.count_of_enemy -= self.power
            print(f'{self.name} сражается {days} осталось {self.count_of_enemy} врагов \n')

        print(f'{self.name} одержал победу спустя {days} дней(дня)\n')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
threads = first_knight, second_knight
for thread in threads:
    thread.join()
print('Все битвы кончились')
