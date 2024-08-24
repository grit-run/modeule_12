import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("runner1")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("runner2")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_list = [Runner("runner3"), Runner("runner4")]
        for runner in runner_list:
            for _ in range(10):
                runner.walk()
                runner.run()
        self.assertNotEqual(runner_list[0].distance, runner_list[1].distance)
