import unittest


def pass_if_frozen(fn):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return fn(self, *args, **kwargs)
    return wrapper


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

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


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @pass_if_frozen
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


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = [
            Runner("Usain", 10),
            Runner("Andrew", 9),
            Runner("Nick", 3),
        ]

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print("{}:".format(key))
            for k, v in value.items():
                print("{}: {}".format(k, v))

    def test_tournament1(self):
        turn_1 = Tournament(90, self.runners[0], self.runners[2])
        result = turn_1.start()
        self.assertTrue(list(result.values())[-1].name == "Nick")
        self.all_results["Результат первого забега"] = result

    def test_tournament2(self):
        turn_2 = Tournament(90, self.runners[1], self.runners[2])
        result = turn_2.start()
        self.assertTrue(list(result.values())[-1].name == "Nick")
        self.all_results["Результат второго забега"] = result

    @pass_if_frozen
    def test_tournament3(self):
        turn_3 = Tournament(90, *self.runners)
        result = turn_3.start()
        self.assertTrue(list(result.values())[-1].name == "Nick")
        self.all_results["Результат третьего забега"] = result

    @pass_if_frozen
    def test_tournament4(self):
        distance = 5
        turn_4 = Tournament(distance, *self.runners)
        result = turn_4.start()
        self.assertTrue(list(result.values())[-1].name == "Nick", "Wrong winner on too short distance "
                                                                  "(not more then 6 meters), Nick is still slowest "
                                                                  "runner")
        self.all_results["Результат четвертого забега"] = result
