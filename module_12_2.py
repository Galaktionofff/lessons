import Ex
import unittest
from pprint import pprint


class TestTournament(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner = Ex.Runner('Усэйн', 10)
        self.runner1 = Ex.Runner('Андрей', 9)
        self.runner2 = Ex.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        pprint(cls.all_results)

    def speed_run(self):
        tour = Ex.Tournament(90, self.runner, self.runner2)
        t_s = tour.start()
        self.all_results.append(t_s)
        self.assertTrue(self.all_results[-1] == 'Ник')

    def speed_run1(self):
        tour = Ex.Tournament(90, self.runner1, self.runner2)
        t_s = tour.start()
        self.all_results.append(t_s)
        self.assertTrue(self.all_results[-1] == 'Ник')

    def speed_run2(self):
        tour = Ex.Tournament(90, self.runner, self.runner1, self.runner2)
        t_s = tour.start()
        self.all_results.append(t_s)
        self.assertTrue(self.all_results[-1] == 'Ник')

test = TestTournament()
