import logging
from unittest import TestCase
import unittest
from Ex import Runner
import Ex
from pprint import pprint

logging.basicConfig(filename='runner_test.log', filemode='w',level=logging.INFO,
                    encoding='UTF-8', format='%(levelname)s | %(message)s')


class RunnerTest(TestCase):
        is_frozen = False

        @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
        def test_walk(self):
            try:
                runner = Runner('Nikita', -1)
                for i in range(10):
                    runner.walk()
                self.assertEquals(runner.distance, 50)
                logging.info('"test_walk" выполнен успешно')
            except:
                logging.warning("Неверная скорость для Runner", exc_info=True)



        @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
        def test_run(self):
            try:
                runner = Runner('Stepan', '121,', 21)
                for i in range(10):
                    runner.run()
                self.assertEquals(runner.distance, 100)
                logging.info('"test_run" выполнен успешно')
            except:
                logging.warning("Неверный тип данных для объекта Runner", exc_info=True)




        @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
        def test_challenge(self):
            runner1 = Runner('Ivan')
            runner2 = Runner('Paul')
            for i in range(10):
                runner1.run()
                runner2.walk()
            self.assertNotEquals(runner2.distance, runner1.distance)


class TestTournament(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    is_frozen = True

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner = Ex.Runner('Усэйн', 10)
        self.runner1 = Ex.Runner('Андрей', 9)
        self.runner2 = Ex.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def tearDown(self):
        pprint(self.all_results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_speed_run(self):
        tour = Ex.Tournament(90, self.runner, self.runner2)
        t_s = tour.start()
        self.all_results.update(t_s)
        self.assertTrue(self.all_results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_speed_run1(self):
        tour = Ex.Tournament(90, self.runner1, self.runner2)
        t_s = (tour.start())
        self.all_results.update(t_s)
        self.assertTrue(self.all_results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_speed_run2(self):
        tour = Ex.Tournament(90, self.runner, self.runner1, self.runner2)
        t_s = tour.start()
        self.all_results.update(t_s)
        self.assertTrue(self.all_results[3] == 'Ник')

run = RunnerTest()
test = TestTournament()
