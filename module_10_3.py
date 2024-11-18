class Bank:
    def __init__(self, balance=0, lock=threading.Lock()):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)
            sum_ = int(random.randint(50, 500))
            self.balance += sum_
            print(f"Пополнение: {sum_}. Баланс: {self.balance}")

    def take(self):
        sum_ = int(random.randint(50, 500))
        for i in range(100):
            print(f'Запрос на {sum_}')
            if self.balance >= sum_:
                self.balance -= sum_
                print(f"Снятие: {sum_}. Баланс: {self.balance}")
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
