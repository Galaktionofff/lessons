from unittest import TestCase
from Ex import Runner
class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner('Serega')
        for i in range(10):
            runner.walk()
        self.assertEquals(runner.distance, 50)

    def test_run(self):
        runner = Runner('Stepan')
        for i in range(10):
            runner.run()
        self.assertEquals(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner('Ivan')
        runner2 = Runner('Paul')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEquals(runner2.distance, runner1.distance)

run = RunnerTest()
