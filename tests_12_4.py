import traceback
import unittest
import logging


logging.basicConfig(level=logging.INFO, filemode="w", filename="module_12_4.log", encoding='utf-8', format="%(asctime)s :: line->%(lineno)d :: %(levelname)s :: %(message)s")



class Runner:
    def __init__(self, name, speed=5):
        if speed < 0:
            raise ValueError("\nСкорость не может быть отрицательной, передано {}".format(speed))
        else:
            self.speed = speed
        if not isinstance(name, str):
            raise ValueError("\nИмя может быть только строкой, передано {}".format(name))
        else:
            self.name = name
        self.distance = 0


    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("runner1",-3)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner {}  \n".format(e))
           # logging.warning(traceback.format_exc())


    def test_run(self):
        try:
            runner = Runner(23)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверный тип данных для объекта Runner {}  \n".format(e))
           # logging.warning(traceback.format_exc())


if __name__ == '__main__':
    unittest.main()