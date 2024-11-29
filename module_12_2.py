from unittest import TestCase
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner('Serega')
        for i in range(10):
            runner.walk()
        self.assertEquals(runner.distance, 50)

    def test_challenge(self):
        runner1 = Runner('Ivan')
        runner2 = Runner('Paul')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEquals(runner2.distance, runner1.distance)

run = RunnerTest()
