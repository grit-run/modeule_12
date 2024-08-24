from super_runner import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):

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

    def test_tournament3(self):
        turn_3 = Tournament(90, *self.runners)
        result = turn_3.start()
        self.assertTrue(list(result.values())[-1].name == "Nick")
        self.all_results["Результат третьего забега"] = result

    def test_tournament4(self):
        distance = 5
        turn_4 = Tournament(distance, *self.runners)
        result = turn_4.start()
        self.assertTrue(list(result.values())[-1].name == "Nick", "Wrong winner on too short distance "
                                                                  "(not more then 6 meters), Nick is still slowest "
                                                                  "runner")
        self.all_results["Результат четвертого забега"] = result
